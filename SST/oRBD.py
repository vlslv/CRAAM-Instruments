# External methods
import string, os, struct, glob
import numpy as np
import datetime as dt
import xml.etree.ElementTree as xmlet
from enum import IntEnum
from astropy.io import fits

# Our methods
import astronomical_methods as am
import oRBD

class RBD(object):

###############################################################################################
#
#    RBD: A python class to use with SST data. Main objective to create SST level-0 files
#
#    Author:  Guigue@Sampa
#             guigue@craam.mackenzie.br  , guigue@gcastro.net
#             http://www.guigue.gcastro.net
#
#    Change Record :  
#         - 2017-06-15 : First written
#         - 2017-06-17 : time now is python datetime format compatible.
#         - 2017-08-19 : xml files implementation
#
###############################################################################################

    """------------------------------------------------------------------------------------ """

    def timeSpan(self):
        return self.getISOTime(self.Data[0]['time']), self.getISOTime(self.Data[-1]['time'])
        
    
    """-------------------------------------------------------------------------------------"""
    def writeFITS(self):
        fits_fname='sst-'+self.MetaData['SSTType'].lower()+'-'+self.MetaData['ISODate']+'T'+self.MetaData['ISOTime']+'-level0.fits'
        self.MetaData.update({'FITFname':fits_fname})

        hdu = fits.PrimaryHDU()
        hdu.header.append(('origin','CRAAM/Universidade Presbiteriana Mackenzie',''))
        hdu.header.append(('telescop','Solar Submillimeter Telescope',''))
        hdu.header.append(('date-obs',self.MetaData['ISODate'],''))
        _hhmmss_ = self.timeSpan()
        hdu.header.append(('t_start',self.MetaData['ISODate']+'T'+ _hhmmss_[0]))
        hdu.header.append(('t_end',self.MetaData['ISODate']+'T'+ _hhmmss_[1]))
        hdu.header.append(('data_typ',self.MetaData['SSTType']))
        hdu.header.append(('origfile',self.MetaData['RBDFileName']))
        for i in range(len(self.Comments)):
            hdu.header.append(('history',self.Comments[i]))

        for child in self.header:
            
            # xml table. Children have three fields
            _ttype_ = child[0].text        # Name
            _tform_ = child[1].text        # (Dimension) Format
            _tunit_ = child[3].text        # Unit
            _tzero_ = 0                    # Effective 0 (to mimmic an unsigned integer)
            _tscal_ = 1.0                  # Data Scaling Factor
            _tdim_  = int(child[1].text)   # Dimension  
            _VarType_ = child[2].text      # Variable type
                        
            if ( _VarType_ == 'xs:int') : 
                _tform_ += 'J'
                
            if ( _VarType_ == 'xs:unsignedShort') :
                _tform_ += 'I'
                _tzero_ = 32768
                
            if ( _VarType_ == 'xs:short'):
                _tform__ += 'I' 
                
            if ( _VarType_ == 'xs:byte') :
                _tform_ += 'B'
                
            if ( _VarType_ == 'xs:float') :
                _tform_ += 'E'
                
        return hdu
    
    def base_name(self,fname):
        _s_ = fname.strip().split('/')
        return _s_[len(_s_)-1]

    """------------------------------------------------------------------------------------ """

    def getISOTime(self,hustime):
        
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
        for child in self.header:
            
            # xml table. Children have three fields
            _VarName_ = child[0].text                                          # Variable Name
            _VarDim_  = int(child[1].text)                                     # Variable Dimension
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

            bin_header = {'names':_fieldnames_, 'ranges':_ranges_,'fmt':_fmt_}
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

    def cleanRBD(self):
        """

        cleanRBD : is a set of procedures to clean the Raw Binary Data (RBD).  
            This procedures could be applied when reading the record. But for
            readbility reasons I do prefer to do it after the files is completely 
            read. Below a list of procedures.

            1) Clean_null_Data: for some misterious reason, the first
                   record in a Auxiliary file has all values equal to 0. We 
                   remove these records. 

        Change Record:
            First written by Guigue @ Sampa on 2017-08-22

        """
        _removed_rec_ = ''
        _count_ = 0
        for _irec_ in range(len(self.Data)-1):
            if ( self.Data[_irec_]['time'] == 0 ) :
                _nothing_= self.Data.pop(_irec_)
                _removed_rec_+=str(_irec_)+' '
                _count_ = _count_ + 1
        self.Comments.append('Checked for null data')
        if (_count_ > 0) : self.Comments.append('null-data records removed :'+_removed_rec_)
        
        return

    """-------------------------------------------------------------------------- """
    
    def readRBD(self):

        self.define_fmt()
        _fmt_    = self.bin_header['fmt']
        _header_ = self.bin_header['names']
        _ranges_ = self.bin_header['ranges']
        _Nfields_= len(_header_)
        
        if os.path.exists(self.fname) :
            _fd_         = os.open(self.fname,os.O_RDONLY)
            _nrec_       = os.fstat(_fd_).st_size / struct.calcsize(_fmt_)
            for _irec_ in range(_nrec_) :
                _record_      = {}
                _one_record_  = os.read(_fd_,struct.calcsize(_fmt_))
                _ur_          = struct.unpack(_fmt_,_one_record_)
                for _field_ in range(_Nfields_):
                    if (_ranges_[_field_][0] == _ranges_[_field_][1]) :
                        _record_.update({_header_[_field_]:_ur_[_ranges_[_field_][0]]})
                    else:
                        _record_.update({_header_[_field_]:_ur_[_ranges_[_field_][0]:_ranges_[_field_][1]+1]})
                self.Data.append(_record_)
            os.close(_fd_)
        else:
            print 'File '+fname+'  not found'

        self.Comments.append('Converted to FITS level-0 with oRBD.py version '+self.version)
        
        return

    """-----------------------------------------------------------------------------"""
    
    def __init__(self,fname='rs19990501'):

        self.fname = fname
        self.Data   = []
        self.MetaData = {}
        self.Comments = []
        self.version = '20170824T23:14'
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
