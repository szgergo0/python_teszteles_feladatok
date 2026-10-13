import math
import unittest

def negyzetgyok(szam):
    
    if szam<0:
        return "Negativ szambol nem vonunk negyzetgyokot!"
    else:
        return math.sqrt(szam)
class Testnegyzet(unittest.TestCase):
    def test_pos(self):
        self.assertGreater(negyzetgyok(3), 0)
    def test_neg(self):
        self.assertEqual(negyzetgyok(-2), "Negativ szambol nem vonunk negyzetgyokot!")


if __name__ == '__main__':
    unittest.main()
