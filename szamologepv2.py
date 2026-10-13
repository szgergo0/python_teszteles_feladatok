
import unittest

def muveletek(x, y ,a):
    jel="+-*/"
    if a in jel:
        if a == "*":
            return x*y
        elif a == "-":
            return x-y
        elif a == "+":
            return x+y
        elif a == "/":
            if y != 0:
                return x/y
            else:
                return "Nullaval nem osztunk"
    else:
        return "Nem helyes a jel"

class Testfgv(unittest.TestCase):
    def test_10_0(self):
        self.assertEqual(muveletek(10, 0, "/"), "Nullaval nem osztunk")
    def test_4_neg5(self):
        self.assertLess(muveletek(4, -5, "+"), 0)
    def test_neg_neg5(self):
        self.assertGreater(muveletek(-5, -5, "*"), 0)
    def test_neg_minusz_neg(self):
        self.assertGreater(muveletek(-4, -5, "-"), 0)
    def test_100_10_kiv(self):
        self.assertEqual(muveletek(100, 10, "-"), 90)
    def test_100_10_osszead(self):
        self.assertEqual(muveletek(100, 10, "+"), 110)
    def test_100_10_szorzas(self):
        self.assertEqual(muveletek(100, 10, "*"), 1000)
    def test_100_10_osztas(self):
        self.assertEqual(muveletek(100, 10, "/"), 10)
    

if __name__ == "__main__":
    unittest.main()