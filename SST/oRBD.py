# External methods
import string, os, struct, glob
import numpy as np
import datetime as dt
import xml.etree.ElementTree as xmlet
from enum import IntEnum

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

        try:
            _name1_,_name2_=fname.strip().split(".")
        except:
            _name1_ = fname.strip()
            _name2_ = ''
            
        if (_name1_[0:2].upper() == 'RS') or (_name1_[0:2].upper() == 'RF'):
            type='Data'
        else:
            type='Auxiliary'
            
        if (len(_name1_) == 8):
            date=str(int(_name1_[2:4])+1900) + '-' + _name1_[4:6] + '-' + _name1_[6:8]
        else:
            date=str(int(_name1_[2:5])+1900) + '-' + _name1_[5:7] + '-' + _name1_[7:9]
        return type,date

    """-----------------------------------------------------------------------------"""

    def define_fmt(self,header):
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
        for child in header:
            
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
        return bin_header

    def read_xml_header(self,fname):
        _tt_        = oRBD.DataTimeSpan()
        _ISODate_   = self.getISODate(fname)
        _hfname_    = _tt_.findHeaderFile(SSTType=_ISODate_[0],SSTDate=_ISODate_[1])
        _xmlheader_ = xmlet.parse(_hfname_)
        self.hfname = _hfname_
        self.header = _xmlheader_.getroot()
        return 
    
    def __init__(self,fname='rs19990501'):

        self.read_xml_header(fname)
        
        self.data   = []
        self.fname  = fname
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
        
    def findHeaderFile(self,SSTType="Data",SSTDate="1899-12-31"):
        """
        findHeaderFile:
        Given the DataType and the Date, look for the RBD xml description file. 
        I guess there is a better and more efficient way to search in a b-tree, but
        I'm tired to find it ;-)

        Input:
            SSTType = "Data" | "Auxiliary"
            SSTDate = YYYY-MM-DD

        Output:
            a string with the name of the RBD xml decription file.

        Change Record
            First created by Guigue @ Sampa on 2017-08-19 

        """
        DataDescriptionFileName=''
        for child in self.table:
            if (child[0].text == SSTType) and (child[1].text <= SSTDate) and (child[2].text >= SSTDate) :
                DataDescriptionFileName=child[3].text
        return DataDescriptionFileName

    """------------------------------------------------------------------------"""

    def __init__(self):
        _tt_ = xmlet.parse('SSTDataFormatTimeSpanTable.xml')
        self.table = _tt_.getroot()
        return
