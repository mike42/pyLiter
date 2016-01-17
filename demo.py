#!/usr/bin/env python3
from pyLiter.MagickLiter import MagickLiter
from pyLiter.LightState import LightState


#a.values = LightState.clear()

#for i in range(0,9):
#	a.values = LightState.bar(i / 8)
#
#a.values = LightState.clear()

state = LightState([0, 0, 0, 0, 0, 1, 1, 1])
a.values = state
#for i in range(0, 5):
for i in range(15):
    state = state.shiftLeft(1)
    a.values = state
    #for i in range(7):
    #	state = state.shiftRight(1)
    #	a.values = state

#a.clear()
#
#a.values = [0, 0, 0, 0, 1, 0, 0, 0]

#print a.values
#a.blink([1,1,1,1,1,1,1,1])

#print a.values

#a.marquee([0, 1, 0, 1, 0, 1, 0, 1])
#print a.values

