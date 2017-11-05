#!/usr/bin/python

def PrintUsage:
    print '                                                '
    print '------------------------------------------------'
    print '                                                '
    print 'Usage: CorrectAuxiliary [Auxiliary RBDfilename] '
    print '       example = CorrectAuxiliary   bi1171104   '
    print '                                                '
    print '----------------------------------------------- '
    return
    
if __name__ == "__main__":

    import sys, string, os
    import numpy as np
    import matplotlib.pyplot as plt
    import datetime as dt

    import oRBD

    if len(sys.argv) < 2 :
        PrintUsage()
        sys.exit(1)

    RBDfname=sys.argv[1]
    
    d=oRBD.RBD()
    try:
        d.readRBDinDictionary(RBDfname)
    except Exception, e:
        print "An unexpected exception occurred"
        sys.exit(1)

    if (d.MetaData['SSTType'] != 'Auxiliary') :
        PrintUsage()
        sys.exit(1)

    TimeNotZero = np.where(d.Data['time'] != 0)
    
    
