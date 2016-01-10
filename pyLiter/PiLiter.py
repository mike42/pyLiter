import wiringpi2 as wiringpi

from pyLiter import LightHardware

class PiLiter(LightHardware):
    """ Communicate with the actual hardware """
    lightPinMap = [7, 0, 2, 1, 3, 4, 5, 6]

    def __init__(self):
        """ Set up hardware """
        super().__init__()
        wiringpi.wiringPiSetup()
        # Set up each pin for digital output
        for i in self.lightPinMap:
            wiringpi.pinMode(i, 1)

    def updateValue(self, lightId, value):
        pinId = self.lightPinMap[lightId]
        wiringpi.digitalWrite(pinId, value)
