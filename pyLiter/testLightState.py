import unittest
from LightState import LightState

class TestLightState(unittest.TestCase):
    def testShiftLeft(self):
        # Move one place
        a = LightState([0, 0, 0, 1, 0, 0, 0, 0])
        b = a << 1
        self.assertEqual(b._values, [0, 0, 1, 0, 0, 0, 0, 0])
        # Two places
        b = a << 2
        self.assertEqual(b._values, [0, 1, 0, 0, 0, 0, 0, 0])
        # Wrapping
        b = a << 4
        self.assertEqual(b._values, [0, 0, 0, 0, 0, 0, 0, 1])
        # Handling numbers > 8
        b = a << 12
        self.assertEqual(b._values, [0, 0, 0, 0, 0, 0, 0, 1])

    def testShiftRight(self):
        # Move one place
        a = LightState([0, 0, 0, 1, 0, 0, 0, 0])
        b = a >> 1
        self.assertEqual(b._values, [0, 0, 0, 0, 1, 0, 0, 0])
        # Two places
        b = a >> 2
        self.assertEqual(b._values, [0, 0, 0, 0, 0, 1, 0, 0])
        # Wrapping
        b = a >> 4
        self.assertEqual(b._values, [0, 0, 0, 0, 0, 0, 0, 1])
        # Handling numbers > 8
        b = a >> 12
        self.assertEqual(b._values, [0, 0, 0, 0, 0, 0, 0, 1])

    def testEq(self):
        a = LightState([0, 1, 0, 1, 0, 1, 0, 1])
        b = LightState([0, 1, 0, 1, 0, 1, 0, 1])
        c = LightState([0, 1, 0, 1, 0, 1, 0, 0])
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(b, c)
    
    def testAnd(self):
        a = LightState([1, 1, 1, 1, 1, 1, 1, 1])
        b = LightState([0, 0, 0, 0, 0, 0, 0, 0])
        c = LightState([1, 0, 1, 0, 0, 1, 0, 0])
        d = a & b
        self.assertEqual(d._values, [0, 0, 0, 0, 0, 0, 0, 0])
        d = b & c
        self.assertEqual(d._values, [0, 0, 0, 0, 0, 0, 0, 0])
        d = c & a
        self.assertEqual(d._values, [1, 0, 1, 0, 0, 1, 0, 0])

    def testOr(self):
        a = LightState([1, 1, 1, 1, 1, 1, 1, 1])
        b = LightState([0, 0, 0, 0, 0, 0, 0, 0])
        c = LightState([1, 0, 1, 0, 0, 1, 0, 0])
        d = a | b
        self.assertEqual(d._values, [1, 1, 1, 1, 1, 1, 1, 1])
        d = b | c
        self.assertEqual(d._values, [1, 0, 1, 0, 0, 1, 0, 0])
        d = c | a
        self.assertEqual(d._values, [1, 1, 1, 1, 1, 1, 1, 1])

    def testXor(self):
        a = LightState([1, 1, 1, 1, 1, 1, 1, 1])
        b = LightState([0, 0, 0, 0, 0, 0, 0, 0])
        c = LightState([1, 0, 1, 0, 0, 1, 0, 0])
        d = a ^ b
        self.assertEqual(d._values, [1, 1, 1, 1, 1, 1, 1, 1])
        d = b ^ c
        self.assertEqual(d._values, [1, 0, 1, 0, 0, 1, 0, 0])
        d = c ^ a
        self.assertEqual(d._values, [0, 1, 0, 1, 1, 0, 1, 1])

    def testInvert(self):
        a = LightState([1, 1, 1, 1, 1, 1, 1, 1])
        b = LightState([0, 0, 0, 0, 0, 0, 0, 0])
        c = LightState([1, 0, 1, 0, 0, 1, 0, 0])
        d = ~a
        self.assertEqual(d._values, [0, 0, 0, 0, 0, 0, 0, 0])
        d = ~b
        self.assertEqual(d._values, [1, 1, 1, 1, 1, 1, 1, 1])
        d = ~c
        self.assertEqual(d._values, [0, 1, 0, 1, 1, 0, 1, 1])


if __name__ == '__main__':
    unittest.main()
