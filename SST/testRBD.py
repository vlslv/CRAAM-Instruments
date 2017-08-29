# Simple test

import oRBD

d=oRBD.RBD('TestData/bi1010822')
d.readRBDinDictionary()
d.writeFITS()

d=oRBD.RBD('TestData/bi1021019')
d.readRBDinDictionary()
d.writeFITS()

d=oRBD.RBD('TestData/bi1021202')
d.readRBDinDictionary()
d.writeFITS()

d=oRBD.RBD('TestData/bi1021221')
d.readRBDinDictionary()
d.writeFITS()

d=oRBD.RBD('TestData/rs1020715.1300')
d.readRBDinDictionary()
d.writeFITS()

d=oRBD.RBD('TestData/rs1021205.2200')
d.readRBDinDictionary()
d.writeFITS()

d=oRBD.RBD('TestData/rs1061206.2100')
d.readRBDinDictionary()
d.writeFITS()

d=oRBD.RBD('TestData/rs990909.1700')
d.readRBDinDictionary()
d.writeFITS()







