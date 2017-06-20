# A simple test for the scripts

import oSST
d=oSST.SST()
d.data_path='./TestData'
d.initial_time=d.str2datetime('2015-03-09 15')
d.final_time=d.str2datetime('2015-03-9 15:59')
d.data_type='rs'
d.read()

t=oSST.TimeAxis()
t.getTimeAxis(d,'dt')

y=oSST.yAxis()
y.getValues(d,'adc')

import matplotlib.pyplot as plt
plt.plot(t.time,y.adc[:,5])
plt.xlabel('UT')
plt.ylabel(y.AxisName[5]+' ('+y.AxisUnits+')')
plt.show()


#import oSSTMap
#m=oSSTMap.Map(d)
#m.getDataMaps(d)
#tp=oSST.TotalPower()
#tp.getTotalPower(d,oSST.Beams.two)



