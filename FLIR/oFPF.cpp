#include "oFPF.h"

oFPF::oFPF( ) {};

oFPF::~oFPF() {} ;

void oFPF::OpenImage (std::string fname, ifstream &fin ){
  fin.open(fname.c_str(), std::ifstream::in | std::ifstream::binary);
  image.header.fpf_fname=fname;
  return ;
}

void oFPF::CloseImage (ifstream & fin){
  fin.close();
  return;
}


// Read Header 
void oFPF::ReadHeader(ifstream & fin) {
  unsigned int   ibuffer;
  unsigned short sbuffer;
  char  buffer[64];

  fin.read(image.header.image_data.fpfID, 32);

  fin.read((char *) &ibuffer,4); 
  image.header.image_data.version = (unsigned long) (ibuffer) ;

  fin.read((char *) &ibuffer,4);
  image.header.image_data.pixelOffset = (unsigned long) (ibuffer);

  fin.read((char *) &sbuffer,2);
  image.header.image_data.ImageType = (unsigned long) (sbuffer);

  fin.read((char *) &sbuffer,2);
  image.header.image_data.pixelFormat = (unsigned int) (sbuffer);

  fin.read((char *) &sbuffer,2);
  image.header.image_data.xSize = (unsigned int) (sbuffer);

  fin.read( (char *) &sbuffer,2);
  image.header.image_data.ySize = (unsigned int) (sbuffer);

  fin.read((char *) &ibuffer,4);
  image.header.image_data.trig_count = (unsigned long) (ibuffer);

  fin.read((char *) &ibuffer,4);
  image.header.image_data.frame_count = (unsigned long) (ibuffer);

  fin.read(buffer,64);
};

void oFPF::DimensionDataArray(bool noShow=true){
  image.data.resize(image.header.image_data.xSize * image.header.image_data.ySize);
  if (!noShow) 
    cout << endl << "Size of Data Image = " << image.data.size() << endl;
  return;
}

void oFPF::ReadImage(ifstream & fin) {

  char buffer2[64];
  
  /*******************************************************************
   The Camera Data Header 
  ******************************************************************/
  {
    char buffer[32];
    float fbuffer[2];
    
    fin.read(image.header.camdata.camera_name, FPF_CAMERA_TYPE_LEN+1)   ;
    fin.read(image.header.camdata.camera_partn,FPF_CAMERA_PARTN_LEN+1)  ;
    fin.read(image.header.camdata.camera_sn, FPF_CAMERA_SN_LEN+1)       ;
  
    fin.read((char *) &fbuffer,sizeof(float)*2)                         ;
    image.header.camdata.camera_range_tmin = (float) fbuffer[0]         ;
    image.header.camdata.camera_range_tmax= (float) fbuffer[1]          ;
  
    fin.read(image.header.camdata.lens_name,FPF_LENS_TYPE_LEN+1)        ;
    fin.read(image.header.camdata.lens_partn,FPF_LENS_PARTN_LEN+1)      ;
    fin.read(image.header.camdata.lens_sn,FPF_LENS_SN_LEN+1)            ;
    fin.read(image.header.camdata.filter_name,FPF_FILTER_TYPE_LEN+1)    ;
    fin.read(image.header.camdata.filter_partn,FPF_FILTER_PARTN_LEN+1)  ;
    fin.read(image.header.camdata.filter_sn,FPF_FILTER_SN_LEN+1)        ;
    fin.read(buffer2,64)                                                ;
  }
  
  /*******************************************************************
   The Object Parameters Header 
  ******************************************************************/
  {
    float fbuffer[10];
    
    fin.read((char *) &fbuffer,sizeof(float)*10)                ;
    image.header.object_par.emissivity = (float) fbuffer[0]     ;
    image.header.object_par.objectDistance = (float) fbuffer[1] ;
    image.header.object_par.ambTemp = (float) fbuffer[2]        ;
    image.header.object_par.atmTemp = (float) fbuffer[3]        ;
    image.header.object_par.relHum = (float) fbuffer[4]         ;
    image.header.object_par.compuTao = (float) fbuffer[5]       ;
    image.header.object_par.estimTao = (float) fbuffer[6]       ;
    image.header.object_par.refTemp = (float) fbuffer[7]        ;
    image.header.object_par.extOptTemp = (float) fbuffer[8]     ;
    image.header.object_par.extOptTrans = (float) fbuffer[9]    ;

    fin.read(buffer2,64)                                        ;
  }
  
  /*****************************************************************
   The Date Time Header 
  ******************************************************************/
  {
    unsigned int ibuffer[7] ;
    
    fin.read((char *) &ibuffer,sizeof(int)*7)              ;
    image.header.datetime.Year = (long) ibuffer[0]         ;
    image.header.datetime.Month = (long) ibuffer[1]        ;
    image.header.datetime.Day = (long) ibuffer[2]          ;
    image.header.datetime.Hour = (long) ibuffer[3]         ;
    image.header.datetime.Minute = (long) ibuffer[4]       ;
    image.header.datetime.Second = (long) ibuffer[5]       ;
    image.header.datetime.MilliSecond = (long) ibuffer[6]  ;

    fin.read(buffer2,64)                                   ;

  }

  /*******************************************************************
   The Scaling Header 
  ******************************************************************/
  {
  float fbuffer[6];
  fin.read((char *) &fbuffer,sizeof(float)*6)         ;
  image.header.scaling.tMinCam   = (float) fbuffer[0] ;
  image.header.scaling.tMaxCam   = (float) fbuffer[1] ;
  image.header.scaling.tMinCalc  = (float) fbuffer[2] ;
  image.header.scaling.tMaxCam   = (float) fbuffer[3] ;
  image.header.scaling.tMinScale = (float) fbuffer[4] ;
  image.header.scaling.tMaxScale = (float) fbuffer[5] ;
  fin.read(buffer2,64)                                ;
  }

  /***************************************************************
   The actual Data
  ****************************************************************/
  {
    char buffer[32*sizeof(int)];
    fin.read(buffer,32*sizeof(int));
    fin.read(reinterpret_cast<char*>(image.data.data()), image.data.size()*sizeof(float));
  }
  
};

  
void oFPF::ShowHeader(){

  cout << endl << endl << "   Image Header  " << endl ;

  cout << endl << "Image Data" << endl ;
  cout << "fpfID = " << image.header.image_data.fpfID << endl ;
  cout << "version = " << image.header.image_data.version << endl ;
  cout << "pixelOffset = " << image.header.image_data.pixelOffset << endl;
  cout << "ImageType = " << image.header.image_data.ImageType << endl;
  cout << "pixelFormat = " << image.header.image_data.pixelFormat << endl;
  cout << "xSize = " << image.header.image_data.xSize << endl;
  cout << "ySize = " << image.header.image_data.ySize << endl;
  cout << "trig_count = " << image.header.image_data.trig_count << endl;
  cout << "frame_count = " << image.header.image_data.frame_count << endl;
  
  cout << endl << "Camera Data" << endl;
  cout << "Camera Name = " << image.header.camdata.camera_name << endl;
  cout << "Camera Part N = " << image.header.camdata.camera_partn << endl;
  cout << "Camera SN = " << image.header.camdata.camera_sn << endl;
  cout << "Camera Tmin = " << image.header.camdata.camera_range_tmin << endl;
  cout << "Camera Tmax = " << image.header.camdata.camera_range_tmax << endl;
  cout << "Camera Lens name = " << image.header.camdata.lens_name << endl;
  cout << "Camera Lens PartN = " << image.header.camdata.lens_partn << endl;
  cout << "Camera Lens SN = " << image.header.camdata.lens_sn << endl;
  cout << "Camera Filter Name = " << image.header.camdata.filter_name << endl;
  cout << "Camera Filter PartN = " << image.header.camdata.filter_partn << endl;
  cout << "Camera Filter SN = " << image.header.camdata.filter_sn << endl;

  cout << endl << "Object Parameters" << endl;
  cout << "Emisivity = " << image.header.object_par.emissivity << endl ;
  cout << "Object Distance = " << image.header.object_par.objectDistance << endl ;
  cout << "ambTemp = " << image.header.object_par.ambTemp << endl ;
  cout << "atmTemp = " << image.header.object_par.atmTemp << endl ;
  cout << "relHum = " << image.header.object_par.relHum << endl ;
  cout << "compuTao = " << image.header.object_par.compuTao << endl ;
  cout << "estimTao = " << image.header.object_par.estimTao << endl ;
  cout << "refTemp = " << image.header.object_par.refTemp << endl ;
  cout << "extOptTemp = " << image.header.object_par.extOptTemp << endl ;
  cout << "extOptTrans = " << image.header.object_par.extOptTrans << endl ;

  cout << endl << "Date Time Data" << endl ;
  cout << "Year = " << image.header.datetime.Year << " Month = " <<
    image.header.datetime.Month << " Day = " << image.header.datetime.Day << endl;
  cout << "Hour = " << image.header.datetime.Hour << " Minutes = " << image.header.datetime.Minute
       << " Seconds = " << image.header.datetime.Second << " Milliseconds = "
       << image.header.datetime.MilliSecond << endl;

  cout << endl << "Scaling Header " << endl ;
  cout << "tMinCam = " << image.header.scaling.tMinCam << endl ;
  cout << "tMaxCam = " << image.header.scaling.tMaxCam << endl ;
  cout << "tMinCalc = " << image.header.scaling.tMinCalc << endl;
  cout << "tMaxCam = " << image.header.scaling.tMaxCam << endl ;
  cout << "tMinScale = " << image.header.scaling.tMinScale << endl ;
  cout << "tMaxScale = " << image.header.scaling.tMaxScale << endl;

}

float oFPF::getElement(short f, short c)
{
  unsigned long image_index;
  
  if (f < image.header.image_data.ySize && f >= 0 &&
      c < image.header.image_data.xSize && c >= 0 )
    {
      image_index = c + f * image.header.image_data.xSize ;
      return image.data[image_index] ;
    }
   else
     {
       return -999;
     } 

}
      
int oFPF::writeFITS(string & fitsname ) const
{
  char buff1[10], buff2[25];
  string Date_Obs, T_Start;
  long naxis = 2;
  long nelements=0, first_pixel=1;
  long naxes[2] = {image.header.image_data.xSize , image.header.image_data.ySize};

  // CCfits uses std::valarray as data, and I prefer to use std::vector
  // The temporary valarray is used to transfer the data to the fits file.
  valarray<float> temp_data(image.data.data(),image.data.size());
    
  /*
     From the Manual of CCfits-2.5

     Declare auto-pointer to FITS at function scope. 
     Ensures no resources leaked if something fails 
     in dynamic allocation.
  */
  
  std::auto_ptr<CCfits::FITS> pFits(0);

  nelements = naxes[0]*naxes[1] ;

  sprintf(buff1,"%4d-%2.2d-%2.2d",
	  image.header.datetime.Year,
	  image.header.datetime.Month,
	  image.header.datetime.Day);
  Date_Obs=buff1;
  
  sprintf(buff2,"%4d-%2.2d-%2.2dT%2.2d:%2.2d:%2.2d.%3.3dZ",
	  image.header.datetime.Year,
	  image.header.datetime.Month,
	  image.header.datetime.Day,
	  image.header.datetime.Hour,
	  image.header.datetime.Minute,
	  image.header.datetime.Second,
	  image.header.datetime.MilliSecond);
  T_Start=buff2;

  try
    {
  /* 
    From the Manual of CCfits-2.5
     Create a new FITS object, specifying the data 
     type and axes for the primary image. Simultaneously 
     create the corresponding file. This image is float
     data, demonstrating the cfitsio extension to the 
     FITS standard.

  */
      pFits.reset(new CCfits::FITS(fitsname, FLOAT_IMG, naxis, naxes)) ;
    }
  catch (CCfits::FITS::CantCreate)
    {
      return -1;
    }

  /* 
       Kind of Subroutine. It writes the header to the fits file.
       Boring... 
  */

  // These are keywords defined considered mandatory.
  pFits->pHDU().addKey("ORIGIN","CRAAM/UPM"," ");
  pFits->pHDU().addKey("TELESCOP","Mid-IR","  ");
  pFits->pHDU().addKey("FREQ","30","THz");
  pFits->pHDU().addKey("ORIGIFIL",image.header.fpf_fname,"Original FPF File Name");
  pFits->pHDU().addKey("DATE-OBS", Date_Obs," ");
  pFits->pHDU().addKey("T_START", T_Start," ");
  pFits->pHDU().addKey("LVL_NUM","0.0","Raw Data");

  // These are the values obtained from the camera.
  pFits->pHDU().writeComment("Original Image Header Cards");
  pFits->pHDU().addKey("fpfID", image.header.image_data.fpfID," ");
  pFits->pHDU().addKey("version", image.header.image_data.version," ");
  pFits->pHDU().addKey("pxOffset",image.header.image_data.pixelOffset," ");
  pFits->pHDU().addKey("ImgType",image.header.image_data.ImageType," ");
  pFits->pHDU().addKey("pxFormat",image.header.image_data.pixelFormat," ");
  pFits->pHDU().addKey("xSize",image.header.image_data.xSize, " ");
  pFits->pHDU().addKey("ySize",image.header.image_data.ySize," ");
  pFits->pHDU().addKey("trgCount",image.header.image_data.trig_count," ");
  pFits->pHDU().addKey("frmCount",image.header.image_data.frame_count," ");

  pFits->pHDU().writeComment("Camera Data");
  pFits->pHDU().addKey("Name",image.header.camdata.camera_name,"  ");
  pFits->pHDU().addKey("Part_N",image.header.camdata.camera_partn," ");
  pFits->pHDU().addKey("SN",image.header.camdata.camera_sn,"  ");
  pFits->pHDU().addKey("Tmin",image.header.camdata.camera_range_tmin,"  ");
  pFits->pHDU().addKey("Tmax",image.header.camdata.camera_range_tmax,"  ");
  pFits->pHDU().addKey("L_Name",image.header.camdata.lens_name,"Lens Name");
  pFits->pHDU().addKey("L_Part",image.header.camdata.lens_partn,"Lens Part");
  pFits->pHDU().addKey("L_SN",image.header.camdata.lens_sn,"Lens SN");
  pFits->pHDU().addKey("F_Name",image.header.camdata.filter_name,"Filter Name");
  pFits->pHDU().addKey("F_PartN",image.header.camdata.filter_partn,"Filter Part N");
  pFits->pHDU().addKey("F_SN",image.header.camdata.filter_sn,"Filter SN");

  pFits->pHDU().writeComment("Object Parameters");
  pFits->pHDU().addKey("Emisivit",image.header.object_par.emissivity,"  ");
  pFits->pHDU().addKey("ObjDist",image.header.object_par.objectDistance,"Object Distance");
  pFits->pHDU().addKey("ambTemp",image.header.object_par.ambTemp,"  ");
  pFits->pHDU().addKey("atmTemp",image.header.object_par.atmTemp,"  ");
  pFits->pHDU().addKey("relHum",image.header.object_par.relHum,"  ");
  pFits->pHDU().addKey("compuTao",image.header.object_par.compuTao,"  ");
  pFits->pHDU().addKey("estimTao",image.header.object_par.estimTao,"  ");
  pFits->pHDU().addKey("refTemp",image.header.object_par.refTemp,"  ");
  pFits->pHDU().addKey("extOptTemp",image.header.object_par.extOptTemp,"  ");
  pFits->pHDU().addKey("extOptTrans",image.header.object_par.extOptTrans,"  ");

  pFits->pHDU().writeComment("Scaling Header");
  pFits->pHDU().addKey("tMinCam",image.header.scaling.tMinCam," ");
  pFits->pHDU().addKey("tMaxCam",image.header.scaling.tMaxCam," ");
  pFits->pHDU().addKey("tMinCalc",image.header.scaling.tMinCalc," ");
  pFits->pHDU().addKey("tMaxCam",image.header.scaling.tMaxCam," ");
  pFits->pHDU().addKey("tMinScale",image.header.scaling.tMinScale," ");
  pFits->pHDU().addKey("tMaxScale",image.header.scaling.tMaxScale," ");

  pFits->pHDU().write(first_pixel,nelements,temp_data);

  return 0;
  
}
