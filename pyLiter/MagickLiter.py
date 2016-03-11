from __future__ import absolute_import, division, print_function

from pyLiter.LightHardware import LightHardware
from subprocess import call

class MagickLiter(LightHardware):
    """ Write to an image file rather than the real hardware. Used for documentation"""

    def __init__(self):
        """ Set up hardware """
        super(MagickLiter, self).__init__()
        self._seq = 0
        self.size = 18
        self.name = 'outp-'

    def updateValues(self, values):
        self._seq = self._seq + 1
        cmd = [
               "convert",
               "-size",
               "{:d}x{:d}".format(self.size, self.size),
               "canvas:black",
               "-write",
               self.img(0),
               "+delete",
               "-size",
               "{:d}x{:d}".format(self.size, self.size),
               "radial-gradient:yellow",
               "-write",
               self.img(1),
               "+delete",
               self.img(values._values[0]),
               self.img(values._values[1]),
               self.img(values._values[2]),
               self.img(values._values[3]),
               self.img(values._values[4]),
               self.img(values._values[5]),
               self.img(values._values[6]),
               self.img(values._values[7]),
               "+append",
               "{:s}{:03d}.png".format(self.name, self._seq)]
        call(cmd)

    def img(self, val):
        return 'mpr:on' if val == 1 else 'mpr:off'

