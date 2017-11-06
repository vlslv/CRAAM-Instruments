
import numpy as np

def cntgs(s):


    sDim=s.shape[0]
    if (sDim <= 2):
        return np.array([])

    sDiff = s[1:] - s[0:-1]
    tDisc = np.where(sDiff != 1)
    xDisc = np.asarray(tDisc)
    xDisc = xDisc[0]
    nDisc = xDisc.shape[0]

    c     = np.zeros( (nDisc,2), dtype=np.int)
    for i in np.arange(nDisc):
        if (i==0):
            c[0,0] = 0
            c[0,1] = xDisc[0]
        elif (i==nDisc-1):
            c[i,0] = xDisc[i]
            c[i,1] = s.shape[0]
        else:
            c[i,0] = xDisc[i]
            c[i,1] = xDisc[i+1]

    return c
            
