import unittest

class RecentFilesTester(unittest.TestCase):
    def testFirstTimeExecution(self):
        program = Program()
        self.assertEqual(program.getRecentFiles(), [])

if __name__ == '__main__':
    unittest.main()