import poemas

trkf = poemas.open("TestData/SunTrack_120127_120001.TRK")

trkf.to_fits(name="SunTrack_TESTE.fits")

