#!/usr/bin/env python3
from pyLiter.TermLiter import TermLiter
from pyLiter.LightState import LightState
import threading
import time
import Queue
import math
from threading import Lock

class LiterThread (threading.Thread):  
    def __init__(self, liter):
        threading.Thread.__init__(self)
        self.liter = liter
        self.frameRate = 10
        self._shutdown = False
        self._shutdownWhenComplete = False
        self._skip = False
        self.animQueue = Queue.Queue()

    def put(self, animation):
        self.animQueue.put(animation)

    def putFrame(self, item):
        self.enque(LiterThread.wrapFrame(item))

    def run(self):
        # Set up liter and delay
        self.liter.values = LightState.clear()
        delay = 1.0 / self.frameRate;
        while not self._shutdown:
            try:
                a = self.animQueue.get(True, delay)
                if self._skip and not self.animQueue.empty():
                    continue
                self._skip = False
                for i in a():
                    self.liter.values = i
                    if self._shutdown or self._skip:
                        break;
                    time.sleep(delay)
            except Queue.Empty:
                if self._shutdownWhenComplete:
                    self._shutdown = True
                continue
        self._shutdown = True
    
    def stop(self):
        self._shutdown = True
        self.join()
    
    def wait(self):
        self._shutdownWhenComplete = True
        self.join()

    def cutTo(self, animation):
        self.put(animation)
        self._skip = True
    
#    def cutToFrame(self, animation):
#        self.
#        pass
    
    @staticmethod
    def wrapState(state):
        yield state

#class LightAnimation(object):

# TODO some subclassing or something

class SineWaves:
    def __init__(self):
        self.a = 100

    def frames(self):
        for i in range(0, self.a):
            yield LightState.bar(math.sin(i / 5.0) / 2.0 + 0.5)
        # math.sin(i / 100) / 2 + 0.5)

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
