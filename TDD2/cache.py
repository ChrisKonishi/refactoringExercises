import pandas as pd

class Cache():
    def __init__(self):
        self.dataDict = {}
        self.path = "fileTest.txt"

    def getDict(self) -> dict:
        return self.dataDict

    def getData(self,data):
        if data not in self.dataDict:
            myTuple = RealData.getData(self.path,data)
            self.dataDict[data] = myTuple[1]
        
        return (data,self.dataDict[data])

    pass

class RealData():

    @staticmethod
    def getData(path,key):
        csv = pd.read_csv(path)
        for i in range(len(csv)):
            if csv["key"][i] == key:
                return (key,csv["value"][i])
        return ()
