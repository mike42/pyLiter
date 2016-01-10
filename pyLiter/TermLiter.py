from pyLiter.LightHardware import LightHardware

class TermLiter(LightHardware):
    """ Dummy version of the hardware for a terminal. This can be used to test/develop on computers without the piLiter """
    lightPinMap = [7, 0, 2, 1, 3, 4, 5, 6]

    def __init__(self):
        """ Set up hardware """
        super(TermLiter, self).__init__()

    def updateValues(self, values):
        print(self._values._values)
