import unittest
from LightState import LightState

class TestLightState(unittest.TestCase):
    def testShiftLeft(self):
        # Move one place
        a = LightState([0, 0, 0, 1, 0, 0, 0, 0])
        b = a.shiftLeft(1)
        self.assertEqual(b._values, [0, 0, 1, 0, 0, 0, 0, 0])
        # Two places
        b = a.shiftLeft(2)
        self.assertEqual(b._values, [0, 1, 0, 0, 0, 0, 0, 0])
        # Wrapping
        b = a.shiftLeft(4)
        self.assertEqual(b._values, [0, 0, 0, 0, 0, 0, 0, 1])
        # Handling numbers > 8
        b = a.shiftLeft(12)
        self.assertEqual(b._values, [0, 0, 0, 0, 0, 0, 0, 1])

    def testShiftRight(self):
        # Move one place
        a = LightState([0, 0, 0, 1, 0, 0, 0, 0])
        b = a.shiftRight(1)
        self.assertEqual(b._values, [0, 0, 1, 0, 0, 0, 0, 0])
        # Two places
        b = a.shiftRight(2)
        self.assertEqual(b._values, [0, 1, 0, 0, 0, 0, 0, 0])
        # Wrapping
        b = a.shiftRight(4)
        self.assertEqual(b._values, [0, 0, 0, 0, 0, 0, 0, 1])
        # Handling numbers > 8
        b = a.shiftRight(12)
        self.assertEqual(b._values, [0, 0, 0, 0, 0, 0, 0, 1])

    def testEq(self):
        a = LightState([0, 1, 0, 1, 0, 1, 0, 1])
        b = LightState([0, 1, 0, 1, 0, 1, 0, 1])
        c = LightState([0, 1, 0, 1, 0, 1, 0, 0])
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(b, c)

if __name__ == '__main__':
    unittest.main()
