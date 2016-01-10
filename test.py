#!/usr/bin/env python3
from pyLiter.TermLiter import TermLiter
from pyLiter.LightState import LightState

a = TermLiter()

a.values = LightState.clear()

a.values = LightState.bar(0.5)

#a.clear()
#
#a.values = [0, 0, 0, 0, 1, 0, 0, 0]

#print a.values
#a.blink([1,1,1,1,1,1,1,1])

#print a.values

#a.marquee([0, 1, 0, 1, 0, 1, 0, 1])
#print a.values
