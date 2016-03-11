#!/usr/bin/env python3
import math
from pyLiter.TermLiter import TermLiter
from pyLiter.LiterThread import LiterThread
from pyLiter.LightState import LightState

class SineWaves:
    def __init__(self):
        self.a = 100

    def frames(self):
        for i in range(0, self.a):
            yield LightState.bar(math.sin(i / 5.0) / 2.0 + 0.5)

if __name__ == '__main__':
    liter = TermLiter()
    a = LiterThread(liter)
    a._shutdownWhenComplete = True
    a.start()
    try:
        a.put(SineWaves().frames)
        while a.isAlive():
            a.join(1)
    except KeyboardInterrupt:
        a.stop()

    print("Exiting main thread")
