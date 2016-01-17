class LightState(object):
    """ Maintain a list of light states, provide methods for running calculations over them"""
    size = 8
    _values = [-1, -1, -1, -1, -1, -1, -1, -1]
    
    def __init__(self, vals=[-1, -1, -1, -1, -1, -1, -1, -1]):
        self._values = vals

    def __eq__ (self, other):
        return self._values == other._values

    def __lshift__(self, other):
        curVals = self._values[:]
        for _ in range(other):
            nextVals = curVals[1:]
            nextVals.append(curVals[0])
            curVals = nextVals
        return LightState(curVals)

    def __rshift__(self, other):
        curVals = self._values[:]
        for _ in range(other):
            curVals = [curVals[7]] + curVals[:7]
        return LightState(curVals)

    def __and__(self, other):
        curVals = self._values[:]
        for i in range(8):
            curVals[i] = 0
        #otherVals = other._values
        # TODO implement logicalAnd
        return LightState(self._values)

    def __or__(self, other):
        # TODO implement logicalOr
        return LightState(self._values)

    def __xor__(self, other):
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
