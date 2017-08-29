RBD_bifiles='TestData/'+['bi1010822','bi1021019','bi1021202','bi1021221']

  RBD_rsfiles='TestData/'+['rs1020715.1300','rs1021205.2200',$
                           'rs1061206.2100','rs990909.1700']

  FITS_bifiles = ['sst_auxiliary_2001-08-22T14:04:40.034-23:45:04.714_level0.fits',$
                  'sst_auxiliary_2002-10-19T11:24:39.704-21:37:04.235_level0.fits',$
                  'sst_auxiliary_2002-12-02T02:01:34.154-23:18:05.244_level0.fits',$
                  'sst_auxiliary_2002-12-21T11:15:57.732-22:26:07.212_level0.fits']
  
  FITS_rsfiles = ['sst_integration_2002-07-15T13:24:19.605-13:59:59.592_level0.fits',$
                  'sst_integration_2002-12-05T21:59:58.728-22:08:31.215_level0.fits',$
                  'sst_integration_2006-12-06T20:59:58.423-21:54:05.746_level0.fits',$
                  'sst_integration_1999-09-09T16:59:52.056-17:57:40.420_level0.fits']

  for i=0, n_elements(RBD_bifiles)-1 do begin
     read_sst,rbd,RBD_bifiles[i],/mon,/close,recr=1000000
     trbd=tag_names(rbd)
     
     fits=mrdfits(FITS_bifiles[i],1,h,/unsigned)
     tfits=tag_names(fits)

     if (n_elements(trbd) ne n_elements(tfits)) then begin
        print,''
        print,'Structures are different for files '+RBD_bifiles[i]+' and '+FITS_bifiles[i]
        print,'Aborting....'
        print,''
        stop
     endif

     print,RBD_bifiles[i]+' and '+FITS_bifiles[i]
     for itag=0,n_elements(trbd)-1 do begin
        command='m=moment(rbd.'+trbd[itag]+'-fits.'+tfits[itag]+')'
        r=execute(command)
        if (abs(m[0]) gt 0) then begin
           print,'Tag = '+trbd(itag)+' , '+tfits(itag)
           print,'       Difference = '+string(m[0])+'  sigma = '+string(sqrt(m[1]))
           stop
        endif
        
     endfor
     
  endfor

  for i=0, n_elements(RBD_rsfiles)-1 do begin
     read_sst,rbd,RBD_rsfiles[i],/close,recr=1000000
     trbd=tag_names(rbd)
     
     fits=mrdfits(FITS_rsfiles[i],1,h,/unsigned)
     tfits=tag_names(fits)

     if (n_elements(trbd) ne n_elements(tfits)) then begin
        print,''
        print,'Structures are different for files '+RBD_rsfiles[i]+' and '+FITS_rsfiles[i]
        print,'Aborting....'
        print,''
        stop
     endif

     print,RBD_bifiles[i]+' and '+FITS_bifiles[i]
     for itag=0,n_elements(trbd)-1 do begin
        command='m=moment(rbd.'+trbd[itag]+'-fits.'+tfits[itag]+')'
        r=execute(command)
        if (abs(m[0]) gt 0) then begin
           print,'Tag = '+trbd(itag)+' , '+tfits(itag)
           print, 'Difference = '+string(m[0])+'  sigma = '+string(sqrt(m[1]))
           stop
        endif
        
     endfor
     
  endfor

end
