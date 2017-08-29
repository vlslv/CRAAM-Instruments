import oRBD
d1=oRBD.RBD('TestData/rs1150621.1700')
d2=oRBD.RBD('TestData/rs1150621.1800')
d1.readRBDinDictionary()
d2.readRBDinDictionary()
d=oRBD.RBD()
d.concat([d1,d2])    


