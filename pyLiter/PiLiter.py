import wiringpi2 as wiringpi

class PiLiter(object):
    """ Communicate with the actual hardware """
    size = 8
    lightPinMap = [7, 0, 2, 1, 3, 4, 5, 6]

    def __init__(self):
        wiringpi.wiringPiSetup()
        # Set up each pin for digital output
        for i in self.lightPinMap:
            wiringpi.pinMode(i, 1)

    def set(self, lightId, lightValue):
        if lightId < 0 or lightId > 7:
            raise ValueError('LED id must be 0-7')
        if lightValue != 0 and lightValue != 1:
            raise ValueError('Light value must be 0 (off) or 1 (on)')
        # Map light ID to pin ID and set to value
        pinId = self.lightPinMap[lightId]
        wiringpi.digitalWrite(pinId, lightValue)

