from __future__ import absolute_import, division, print_function

from pyLiter.LightState import LightState
import threading
import time
import queue

class LiterThread (threading.Thread):  
    def __init__(self, liter):
        threading.Thread.__init__(self)
        self.liter = liter
        self.frameRate = 10
        self._shutdown = False
        self._shutdownWhenComplete = False
        self._skip = False
        self.animQueue = queue.Queue()

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
            except queue.Empty:
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
    
    @staticmethod
    def wrapState(state):
        yield state
