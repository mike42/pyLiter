from __future__ import absolute_import, division, print_function

from pyLiter.LightState import LightState
import abc

class LightHardware(object):
    def __init__(self):
        self._values = LightState()

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        """ Set values """
        changes = self._values.diff(values)
        self._values = values
        self.updateValues(self._values)
        for lightId in changes:
            self.updateValue(lightId, changes[lightId])

    @abc.abstractmethod
    def updateValue(self, lightId, value):
        """ Send updated light value to the hardware """
        pass

    @abc.abstractmethod
    def updateValues(self, values):
        """ Display updated values to the user (for testing) """
        pass
