from pyLiter.PiLiter import PiLiter

class Lights(object):
    """ Maintain status of the lights """
    def __init__(self, device = PiLiter()):
        size = device.size
        self.device = device
        self._values = [-1]*size

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        """ Set values """
        # TODO values has same len as self._values
        for i in range(len(self._values)):
            self.setValue(i, values[i])

    def clear(self):
        """ Switch off all lights """
        self.values = [0]*len(self._values)

    def bar(self, value, invert = False):
        """ Draw a bar chart with the lights. Optionally
             use 'invert' to change direction """
        # TODO value in range 0-1.
        size = len(self._values)
        # TODO rounding
        count = (int)(size * value)
        newVal = [0]*size
        for i in range(count):
            idx = size - i - 1 if invert else i
            newVal[idx] = 1
        self.values = newVal

    # TODO blink. Currently just sets value to value1
    def blink(self, value1 = None, value2 = None):
        if value1 == None:
            value1 = [1]*len(self._values)
        if value2 == None:
            value2 = [0]*len(self._values)
        self.values = value1

    # TODO marquee. Currently just uses the first n digits
    def marquee(self, value, repeat, reverse):
        self.values = value[0:8]

    # TODO set up frames. These will be chopped out into a list of states.
    def frame(self, value, repeat):
        self.values = value[0:8]

    def cleanse(self, values):
        # Correct the length of an array to match the number of lights
        return values[0:self.size]

    def setValue(self, lightId, lightValue):
        if self._values[lightId] != lightValue:
            self.device.set(lightId, lightValue)
        self._values[lightId] = lightValue

