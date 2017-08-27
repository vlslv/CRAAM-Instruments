# External methods

import sys, string, os, struct, glob
import numpy as np
import xml.etree.ElementTree as xmlet
from astropy.io import fits

# Our methods
import oRBD

class RBD(object):

###############################################################################################
#
#    RBD: A python class to use with SST data, its main objective is to create SST level-0 files
#
#    Author:  Guigue@Sampa
#             guigue@craam.mackenzie.br  , guigue@gcastro.net
#             http://www.guigue.gcastro.net
#
#    Use:
#            >>> import oRBD
#            >>> d=oRBD.RBD('rs1150309.1500')
#            >>> d.readRBDinDictionary()
#            >>> d.writeFITS()
#            Check
#            >>> from astropy.io import fits
#            >>> h=fits.open(fname.fits)
#            >>> print h.info()
#            >>> print(repr(h[0].header))             # Primary Header
#            >>> print(repr(h[1].header))             # Table header
#            >>> h[1].data                            # Actual Data
#
#    Change Record :  
#         - 2017-06-15 : First written
#         - 2017-08-19 : xml files implementation
#         - 2017-08-26 : writeFITS implementation
#
###############################################################################################

    """------------------------------------------------------------------------------------ """

    def timeSpan(self):
        """
        timeSpan:
             looks for the first and last non-zero time in the time array and converts to
             ISO time (HH:MM:SS.SSS)

        Change Record:
             First written by Guigue @ Sampa - 2017-08-26

        """
        _nonzero_=self.Data['time'].nonzero()
        return self.getISOTime(self.Data['time'][_nonzero_[0][0]]) ,self.getISOTime(self.Data['time'][_nonzero_[0][-1]])
        
    
    """-------------------------------------------------------------------------------------"""
    def base_name(self,fname):
        """
        base_name:
            Simple procedure to get the base name of a full described file name
            /path/to/file/filename --> filename

        Change Record:
            Guigue @ Sampa - 2017-08-26

        """
        _s_ = fname.strip().split('/')
        return _s_[len(_s_)-1]

    """------------------------------------------------------------------------------------ """

    def getISOTime(self,hustime):
        """
        getISOTime:
           Convert from Hus (hundred of microseconds) to HH:MM:SS.SSSS

        inputs: 
           hustime : a 4bytes integer with the time in hundred of microseconds since 0 UT. 
                     hustime is the SST time format.

        Change Record:
           First written Guigue @ Sampa - 2017-08-26

        """
        _hours_ = hustime / 36000000
        _minutes_ = (hustime % 36000000) / 600000
        _secs_ = (hustime - (_hours_ * 36000000 + _minutes_ * 600000)) / 10000.0
        return '{0:=02d}'.format(_hours_)+':'+ '{0:=02d}'.format(_minutes_) +':'+'{0:=06.3f}'.format(_secs_)

    """ -------------------------------------------------------------------------------------"""
    
    def getISODate(self,fname):
        """ 
        getISODate:
        Converts an SST filename in a ISO Date format. e.g.: RS1070812.1500 -> 2007-08-12
        It also sets the data type to Data (for RS and RF files) and Auxiliary (for BI)

        Input:
        the SST filename. 

        Output:
        A vector [Type,ISODate]

        Change Record:
        First written by Guigue @ Sampa on 2017-08-19
        """
        _bname_=self.base_name(fname)                                        # Get the base name (remove /path/to/file )
        try:
            _name1_,_name2_=_bname_.strip().split(".")                       # Does it have hours?
        except:
            _name1_ = _bname_.strip()
            _name2_ = ''

        _SSTprefix_ = _name1_[0:2].upper()
        _SSTtype_ = ''
    
        if (_SSTprefix_ == 'RS'): SSTtype='Integration'
        if (_SSTprefix_ == 'RF'): SSTtype='Subintegration'
        if (_SSTprefix_ == 'BI'): SSTtype='Auxiliary'
            
        if (len(_name1_) == 8):
            date=str(int(_name1_[2:4])+1900) + '-' + _name1_[4:6] + '-' + _name1_[6:8]
        else:
            date=str(int(_name1_[2:5])+1900) + '-' + _name1_[5:7] + '-' + _name1_[7:9]
        if (len(_name2_) == 4) :
            time=_name2_[0:2]+':'+_name2_[2:4]
        else:
            time='00:00'
        
        self.MetaData.update({'RBDFileName' : _bname_})
        self.MetaData.update({'ISODate'     : date   })
        self.MetaData.update({'ISOTime'     : time   })
        self.MetaData.update({'SSTType'     : SSTtype})
        
        return type,date

    """-----------------------------------------------------------------------------"""

    def define_fmt(self):
        """

        define_fmt:
        It defines three elements to be used for reading  the raw binary data (RBD) files.
        1) fmt: The binary format in pythons rules. It is a string. With this string python
                can read one record and put it in a list (vector) of 'unpacked' data
        2) ranges : it is a list of 2-members lists. Every member points to the begginning and the end
                    of a variable in the 'unpacked' list (vector)
        3) fieldnames : it is a list of field names in the binary file. It will be used to create the FITS 
                        header

        Change Record:
        First created by Guigue @ Sampa 2017.08.20 : checked against the xml files only.  

        """
        # Internal variables destroyed at the end of procedure
        _fmt_        = '='
        _fieldnames_ = []
        _ranges_     = []
        _fielditer_  = 0
        _TotalDim_   = 0
        
        for child in self.header:
            
            # xml table. Children have three fields
            _VarName_ = child[0].text                                          # Variable Name
            _VarDim_  = int(child[1].text)                                     # Variable Dimension
            _TotalDim_ += _VarDim_
            _VarType_ = child[2].text                                          # Variable type

            _fieldnames_.append(_VarName_)
            _ranges_.append([_fielditer_,_fielditer_+_VarDim_-1])
            _fielditer_+=_VarDim_
            
            for i in range(_VarDim_):
                # A short table that converts from xml types to python bynary formats 
                if ( _VarType_ == 'xs:int')           : _fmt_ = _fmt_ + 'i'  # a 4 bytes integer
                if ( _VarType_ == 'xs:unsignedShort') : _fmt_ = _fmt_ + 'H'  # a 2 bytes unsigned integer
                if ( _VarType_ == 'xs:short')         : _fmt_ = _fmt_ + 'h'  # a 2 bytes integer
                if ( _VarType_ == 'xs:byte')          : _fmt_ = _fmt_ + 'B'  # a byte 
                if ( _VarType_ == 'xs:float')         : _fmt_ = _fmt_ + 'f'  # a 4 bytes float

            bin_header = {'names':_fieldnames_, 'ranges':_ranges_,'fmt':_fmt_,'TotalDim':_TotalDim_}
            self.bin_header=bin_header
        return

    """-----------------------------------------------------------------------------------------"""
    
    def read_xml_header(self,fname):
        self.getISODate(fname)       
        _tt_        = oRBD.DataTimeSpan()
        _hfname_    = _tt_.findHeaderFile(SSTType=self.MetaData['SSTType'],SSTDate=self.MetaData['ISODate'])
        _xmlheader_ = xmlet.parse(_hfname_)
        self.hfname = _hfname_
        self.header = _xmlheader_.getroot()
        return
    
    """-----------------------------------------------------------------------------"""
    
    def readRBDinDictionary(self):
        """
        readRBDinDictionary
           It is the class method used to read a SST Raw Binary Data (RBD). The data is
           represented with a dictionary, each element represents one SST variable, and data 
           is stored in a numpy ndarray. Every ndarray has the python dtype corresponding to 
           the original SST data. 

        Change Record:
           First Written by Guigue @ Sampa - 2017-08-26

        """

        self.define_fmt()
        _fmt_    = self.bin_header['fmt']
        _header_ = self.bin_header['names']
        _ranges_ = self.bin_header['ranges']
        _Nfields_= len(_header_)
        
        if os.path.exists(self.fname) :
            _fd_         = os.open(self.fname,os.O_RDONLY)
            _nrec_       = os.fstat(_fd_).st_size / struct.calcsize(_fmt_)
            
            for _field_ in range(_Nfields_):
                
                if _fmt_[_field_+1] == 'i' : _nptype_=np.int32
                if _fmt_[_field_+1] == 'H' : _nptype_=np.uint16
                if _fmt_[_field_+1] == 'h' : _nptype_=np.int16
                if _fmt_[_field_+1] == 'B' : _nptype_=np.byte
                if _fmt_[_field_+1] == 'f' : _nptype_=np.float32
            
                if ( _ranges_[_field_][0] == _ranges_[_field_][1]):
                    self.Data.update( {_header_[_field_] : np.array(np.empty([_nrec_],_nptype_)) })
                else:
                    _sec_dim_ = _ranges_[_field_][1]-_ranges_[_field_][0]+1
                    self.Data.update( {_header_[_field_] : np.array(np.empty([_nrec_,_sec_dim_],_nptype_))})
                    

            for _irec_ in range(_nrec_) :
                _one_record_  = os.read(_fd_,struct.calcsize(_fmt_))
                _ur_          = struct.unpack(_fmt_,_one_record_)

                for _field_ in range(_Nfields_):
                    if (_ranges_[_field_][0] == _ranges_[_field_][1]) :
                        self.Data[_header_[_field_]][_irec_]= _ur_[_ranges_[_field_][0]]
                    else:
                        self.Data[_header_[_field_]][_irec_,...] = _ur_[_ranges_[_field_][0]:_ranges_[_field_][1]+1]
                            
            os.close(_fd_)
        else:
            print 'File '+fname+'  not found'

        self.Comments.append('Converted to FITS level-0 with oRBD.py version '+self.version)
        
        return
        
    """-----------------------------------------------------------------------------"""
    def writeFITS(self):

        """
        writeFITS:
             A method class to write the SST data as a FITS file. The fits format used is a binary table. 
             Then the file has a primary and a table header. It also defines the name of the fits file as

             sst_[integration | subintegration | auxiliary]_YYYY-MM-DDTHH:MM:SS.SSS-HH:MM:SS.SSS_level0.fits

             integration is a RS file, subintegration is a RF file and auxiliary is a BI file
        
        Change Record:
             First written by Guigue @ Sampa - 2017-08-26
        
        """

        _hhmmss_ = self.timeSpan()
        
        _fits_fname_ = 'sst_'  + self.MetaData['SSTType'].lower() + '_' + self.MetaData['ISODate'] + 'T' + _hhmmss_[0]+'-' + _hhmmss_[1] + '_level0.fits'
        
        self.MetaData.update({'FITSfname':_fits_fname_})

        _hdu_ = fits.PrimaryHDU()
        _hdu_.header.append(('origin','CRAAM/Universidade Presbiteriana Mackenzie',''))
        _hdu_.header.append(('telescop','Solar Submillimeter Telescope',''))
        _hdu_.header.append(('observat','CASLEO',''))
        _hdu_.header.append(('station','Lat = -31.79897222, Lon = -69.29669444, Height = 2.491 km',''))
        _hdu_.header.append(('tz','-3',''))

        _hdu_.header.append(('date-obs',self.MetaData['ISODate'],''))
        _hdu_.header.append(('t_start',self.MetaData['ISODate']+'T'+ _hhmmss_[0],''))
        _hdu_.header.append(('t_end',self.MetaData['ISODate']+'T'+ _hhmmss_[1],''))
        _hdu_.header.append(('data_typ',self.MetaData['SSTType'],''))
        _hdu_.header.append(('origfile',self.MetaData['RBDFileName'],''))
        _hdu_.header.append(('frequen','212 GHz ch=1,2,3,4; 405 GHz ch=5,6',''))

        _hdu_.header.append(('comment','Time is in hundred of microseconds (Hus) since 0 UT',''))
        _hdu_.header.append(('comment','ADCu = Analog to Digital Conversion units. Proportional to Voltage',''))
        _hdu_.header.append(('comment','mDeg = milli degree',''))
        _hdu_.header.append(('comment','Temperatures are in Celsius',''))
                            
        for i in range(len(self.Comments)):
            _hdu_.header.append(('history',self.Comments[i]))

        _fits_cols_ = []
        for _child_ in self.header:
            
            # xml table. Children have three fields
            _ttype_   = _child_[0].text        # Name
            _tform_   = _child_[1].text        # (Dimension) Format
            _tunit_   = _child_[3].text        # Unit
            _tzero_   = 0                    # Effective 0 (to mimmic an unsigned integer)
            _tscal_   = 1.0                  # Data Scaling Factor
            _tdim_    = _child_[1].text        # Dimension  
            _VarType_ = _child_[2].text      # Variable type
                        
            if ( _VarType_ == 'xs:int') : 
                _tform_ += 'J'
                _np_form_ = np.dtype('i4')
                
            if ( _VarType_ == 'xs:unsignedShort') :
                _tform_ += 'I'
                _tzero_ = 32768
                _np_form_ = np.dtype('u2')
                
            if ( _VarType_ == 'xs:short'):
                _tform_ += 'I'
                _np_form_ = np.dtype('i2')
                
            if ( _VarType_ == 'xs:byte') :
                _tform_ += 'B'
                _np_form_=np.dtype('b')
                
            if ( _VarType_ == 'xs:float') :
                _tform_ += 'E'
                _np_form_=np.dtype('f4')

            _c_ = fits.Column(name   = _ttype_  ,
                              format = _tform_  ,
                              unit   = _tunit_  ,
                              bscale = _tscal_  ,
                              bzero  = _tzero_  ,
                              dim    = _tdim_   ,
                              array  = self.Data[_ttype_])
            _fits_cols_.append(_c_)
                
        _coldefs_ = fits.ColDefs(_fits_cols_)
        _tbhdu_   = fits.BinTableHDU.from_columns(_coldefs_)
        _hduList_ = fits.HDUList([_hdu_,_tbhdu_])
        
        if os.path.exists(_fits_fname_) :
            print 'File '+_fits_fname_+ 'already exist. Aborting....'
            sys.exit(1) 
        else:
            _hduList_.writeto(_fits_fname_)
            
        return 

    """------------------------------------------------------------------------------------ """

    def __init__(self,fname='rs19990501'):

        self.fname = fname
        self.Data   = {}
        self.MetaData = {}
        self.Comments = []
        self.version = '20170826T20:35'
        self.read_xml_header(fname)
        return 

######################################################################################

class DataTimeSpan(object):
    """

    DataTimeSpan

    This class has the unique effect of reading the SSTDataFormatTimeSpanTable
    and find the right RBD xml description file. 

    Example of use:
       import oRBD
       tt=oRBD.DataTimeSpan()
       type='Auxiliary'
       date='2017-08-19'
       print tt.findHeaderFile(SSTType=type,SSTDate=date)

    Change Record:

        Firts created by Guigue @ Sampa on 2017.08.19 (very cold indeed)

    """    
        
    def findHeaderFile(self,SSTType="Integration",SSTDate="1899-12-31"):
        """
        findHeaderFile:
        Given the DataType and the Date, look for the RBD xml description file. 
        I guess there is a better and more efficient way to search in a b-tree, but
        I'm tired to find it ;-)

        Input:
            SSTType = "Subintegration" | "Integration" | "Auxiliary"
            SSTDate = YYYY-MM-DD

        Output:
            a string with the name of the RBD xml decription file.

        Change Record
            First created by Guigue @ Sampa on 2017-08-19 
            Corrected on 2017-08-24

        """
        DataDescriptionFileName=''
        if (SSTType == 'Integration') or (SSTType == 'Subintegration') :
            filetype='Data'
        else:
            filetype='Auxiliary'
            
        for child in self.table:
            if (child[0].text == filetype) and (child[1].text <= SSTDate) and (child[2].text >= SSTDate) :
                DataDescriptionFileName=child[3].text
        return DataDescriptionFileName

    """------------------------------------------------------------------------"""

    def __init__(self):
        _tt_ = xmlet.parse('SSTDataFormatTimeSpanTable.xml')
        self.table = _tt_.getroot()
        return
