import unittest
from Program import Program

class RecentFilesTester(unittest.TestCase):
    def testFirstTimeExecution(self):
        program = Program()
        self.assertEqual(program.getRecentFiles(), [])

    def testOpenOneFile(self):
        program = Program()
        program.open("file.txt")
        self.assertEqual(program.getRecentFiles(), ["file.txt"])

    def testDuplicatedFiles(self):
        program = Program()
        program.open("file.txt")
        program.open("peixe.txt")
        program.open("file.txt")
        self.assertEqual(program.getRecentFiles(), ["peixe.txt", "file.txt"])

    def testLimitFiles(self):
        program = Program()
        with open("fileTest.txt", "r") as file:
            for line in file:
                program.open(line[0:-1])

        self.assertEqual(
            program.getRecentFiles(),
            ['peixe.txt','santanche.txt','osu.exe','cyberpunk.txt','rambo.py','foo.txt','igor.py','sugoidesu.txt','bakamitai.mp3', 'kurisu.txt']
        )

if __name__ == '__main__':
    unittest.main()