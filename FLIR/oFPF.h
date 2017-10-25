#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <valarray>
#include <cmath>
#include <CCfits/CCfits>

using namespace std ; 

#ifndef oFPF_H_
#define oFPF_H_

const short FPF_CAMERA_TYPE_LEN  = 31  ;  // Camera name string 
const short FPF_CAMERA_PARTN_LEN = 31  ;  // Camera part number string 
const short FPF_CAMERA_SN_LEN    = 31  ;  // Scanner serial number string 
const short FPF_LENS_TYPE_LEN    = 31  ;  // Lens name string 
const short FPF_LENS_PARTN_LEN   = 31  ;  // Lens part number string 
const short FPF_LENS_SN_LEN      = 31  ;  // Lens serial number string 
const short FPF_FILTER_TYPE_LEN  = 31  ;  // Filter name string 
const short FPF_FILTER_PARTN_LEN = 31  ;  // Filter part number string 
const short FPF_FILTER_SN_LEN    = 31  ;  // Filter serial number string 

const int   FPF_HEADER_SIZE      = 120 ;  // Header size in bytes

struct  FPF_IMAGE_DATA_T
{
  char fpfID[32]                ; // "FLIR Public Image Format" 
  unsigned long version         ;             
  unsigned long pixelOffset     ; // Offset to pixel values from start of fpfID.   
  unsigned long ImageType       ; // Temperature = 0, 
                                  // Diff Temp = 2, 
                                  // Object Signal = 4,
                                  // Diff Object Signal = 5, etc 
  unsigned int pixelFormat      ; // 0 = short integer = 2 bytes
                                  // 1 = long integer = 4 bytes 
                                  // 2 = float (single precision)  = 4 bytes
                                  // 3 = double (double precision) = 8 bytes 
  unsigned int xSize            ;
  unsigned int ySize            ;
  unsigned long trig_count      ; // external trig counter 
  unsigned long frame_count     ; // frame number in sequence 
  unsigned long spareLong[16]   ; // = 0 
} ;

struct FPF_CAMDATA_T {
  char  camera_name[FPF_CAMERA_TYPE_LEN+1]   ;
  char  camera_partn[FPF_CAMERA_PARTN_LEN+1] ;
  char  camera_sn[FPF_CAMERA_SN_LEN+1]       ;
  float camera_range_tmin                    ;
  float camera_range_tmax                    ;
  char  lens_name[FPF_LENS_TYPE_LEN+1]       ;
  char  lens_partn[FPF_LENS_PARTN_LEN+1]     ;
  char  lens_sn[FPF_LENS_SN_LEN+1]           ;
  char  filter_name[FPF_FILTER_TYPE_LEN+1]   ;
  char  filter_partn[FPF_FILTER_PARTN_LEN+1] ;
  char  filter_sn[FPF_FILTER_SN_LEN+1]       ;
};

struct FPF_OBJECT_PAR_T
{
  float emissivity          ; // 0 - 1 
  float objectDistance      ; // Meters 
  float ambTemp             ; // Reflected Ambient temperature in Kelvin 
  float atmTemp             ; // Atmospheric temperature in Kelvin 
  float relHum              ; // 0 - 1 
  float compuTao            ; // Computed atmospheric transmission 0 - 1
  float estimTao            ; // Estimated atmospheric transmission 0 - 1
  float refTemp             ; // Reference temperature in Kelvin 
  float extOptTemp          ; // Kelvin 
  float extOptTrans         ; // 0 - 1 
} ;

struct FPF_DATETIME_T {
   long Year          ;
   long Month         ;
   long Day           ;
   long Hour          ;
   long Minute        ;
   long Second        ;
   long MilliSecond   ;
} ;

struct FPF_SCALING_T {
  float tMinCam               ; //  Camera scale min, in current output 
  float tMaxCam               ; //  Camera scale max 
  float tMinCalc              ; //  Calculated min (almost true min) 
  float tMaxCalc              ; //  Calculated max (almost true max) 
  float tMinScale             ; //  Scale min 
  float tMaxScale             ; //  Scale max 
} ;

struct FPFHEADER_T {
  FPF_IMAGE_DATA_T image_data    ;
  FPF_CAMDATA_T    camdata       ;
  FPF_OBJECT_PAR_T object_par    ;
  FPF_DATETIME_T   datetime      ;
  FPF_SCALING_T    scaling       ;
  string           fpf_fname     ;
} ;

class oFPF {
 private:
  struct image_t {
    FPFHEADER_T header;
    vector <float> data ;
  } image ;
 public:
  oFPF()                                         ;
 ~oFPF()                                         ;
  void OpenImage (std::string , std::ifstream & );
  void CloseImage (std::ifstream & )             ;
  void ReadHeader(std::ifstream &)               ;
  void ReadImage(std::ifstream & )               ;
  void DimensionDataArray(bool)                  ;
  void ShowHeader()                              ;
  float getElement(short , short )               ;
  int  writeFITS(std::string & ) const           ;

} ;

#endif
  
