import unittest
import cache
import time

class CacheTester(unittest.TestCase):
    def testEmpty(self):
        cach = cache.Cache()
        emptyDict = cach.getDict()
        self.assertEqual(emptyDict,{})

    def testfirstKey(self):
        cach = cache.Cache()
        tupla = cach.getData("peixe.txt")
        self.assertEqual(tupla,("peixe.txt",1))

    def testLimit(self):
        cach = cache.Cache()
        tupla = cach.getData("somedaki.txt")
        tupla = cach.getData("peixe.txt")
        tupla = cach.getData("santanche.txt")
        tupla = cach.getData("somedaki.txt")
        tupla = cach.getData("sugoidesu.txt")
        testDict = cach.getDict()
        self.assertDictEqual(testDict,{ "peixe.txt" : 1, "santanche.txt" : 2, "sugoidesu.txt" : 3})

    def testTime(self):
        cach = cache.Cache()
        tupla = cach.getData("somedaki.txt")
        tupla = cach.getData("peixe.txt")
        tupla = cach.getData("santanche.txt")
        tupla = cach.getData("somedaki.txt")
        tupla = cach.getData("sugoidesu.txt")
        testDict = cach.getDict()
        self.assertDictEqual(testDict,{ "peixe.txt" : 1, "santanche.txt" : 2, "sugoidesu.txt" : 3})
        time.sleep(4)
        tupla = cach.getData("igor.py")
        testDict = cach.getDict()
        self.assertDictEqual(testDict, {"igor.py" : 9})


if __name__ == '__main__':
    unittest.main()
