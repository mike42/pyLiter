from __future__ import absolute_import, division, print_function

from pyLiter.LightHardware import LightHardware

class TermLiter(LightHardware):
    """ Dummy version of the hardware for a terminal. This can be used to test/develop on computers without the piLiter """

    def __init__(self):
        """ Set up hardware """
        super(TermLiter, self).__init__()

    def updateValues(self, values):
        print(self._values._values)
