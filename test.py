#!/usr/bin/env python3
from pyLiter.MagickLiter import MagickLiter
from pyLiter.LightState import LightState

a = MagickLiter()

a.values = LightState.clear()

for i in range(0,9):
	a.values = LightState.bar(i / 8)



#a.clear()
#
#a.values = [0, 0, 0, 0, 1, 0, 0, 0]

#print a.values
#a.blink([1,1,1,1,1,1,1,1])

#print a.values

#a.marquee([0, 1, 0, 1, 0, 1, 0, 1])
#print a.values
