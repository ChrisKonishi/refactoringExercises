MAXFILES = 10

class Program:
    def __init__(self):
        self.recentFiles = []

    def getRecentFiles(self):
        return self.recentFiles

    def open(self, path):
        if path in self.recentFiles:
            self.recentFiles.remove(path)

        if len(self.recentFiles) >= MAXFILES:
            del self.recentFiles[0]

        self.recentFiles.append(path)

