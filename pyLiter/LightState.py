class LightState(object):
    """ Maintain a list of light states, provide methods for running calculations over them"""
    size = 8
    _values = [-1, -1, -1, -1, -1, -1, -1, -1]
    
    def __init__(self, vals=[-1, -1, -1, -1, -1, -1, -1, -1]):
        self._values = vals

    def __eq__ (self, other):
        return self._values == other._values

    def shiftLeft(self, num):
        # TODO implement shiftLeft
        return LightState(self._values)

    def shiftRight(self, num):
        # TODO implement shiftRight
        return LightState(self._values)

    def logicalAnd(self, other):
        # TODO implement logicalAnd
        return LightState(self._values)

    def logicalOr(self, other):
        # TODO implement logicalOr
        return LightState(self._values)

    def logicalXor(self, other):
        # TODO implement logicalXor
        return LightState(self._values)

    def logicalNot(self):
        # TODO implement logicalNot
        return LightState(self._values)

    def diff(self, other):
        changes = {}
        for lightId in range(len(self._values)):
            updatedVal = other._values[lightId]
            if updatedVal != -1 and self._values[lightId] != updatedVal:
                changes[lightId] = updatedVal
        return changes

    @staticmethod
    def clear():
        return LightState([0, 0, 0, 0, 0, 0, 0, 0])

    @staticmethod
    def bar(value, invert = False):
        """ Draw a bar chart with the lights. Optionally
             use 'invert' to change direction """
        size = 8
        count = int(round(size * value))
        newVal = [0]*size
        for i in range(count):
            idx = size - i - 1 if invert else i
            newVal[idx] = 1
        return LightState(newVal)