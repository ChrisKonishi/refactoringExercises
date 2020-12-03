import unittest
import cache

class CacheTester(unittest.TestCase):
    def testEmpty(self):
        cach = cache.Cache()
        emptyDict = cach.getDict()
        self.assertEqual(emptyDict,{})

    def testfirstKey(self):
        cach = cache.Cache()
        tupla = cach.getData("peixe.txt")
        self.assertEqual(tupla,("peixe.txt",1))



if __name__ == '__main__':
    unittest.main()
