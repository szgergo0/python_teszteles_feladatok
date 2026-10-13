
import unittest

def parosszamok(x, y):
    osszeg=0
    for i in range(x, y+1):
        if i%2==0:
            osszeg+=i
    return osszeg
class Testfgv(unittest.TestCase):
    def test_42_100(self):
        self.assertEqual(parosszamok(42, 100),2130 )
    def test_00(self):
        self.assertEqual(parosszamok(0, 0),0 )
    def test_2_10(self):
        self.assertEqual(parosszamok(2, 10),30 )
    def test_neg2_10(self):
        self.assertGreater(parosszamok(-2, 10),0 )
    def test_negativszam_negativszam(self):
        self.assertLess(parosszamok(-10, -2),0 )
if __name__ == '__main__':
    unittest.main()