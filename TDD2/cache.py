import pandas as pd
import time
import math

class Cache():
    MAX_VALUES = 3
    TIME_LIMIT = 3

    def __init__(self):
        self.dataDict = {}
        self.timeDict = {}
        self.path = "fileTest.txt"

    def getDict(self) -> dict:
        return self.dataDict

    def getData(self, data: str) -> tuple:
        self.removeOutDated()
        if data not in self.dataDict:
            if(len(self.dataDict) >= self.MAX_VALUES):
                self.removeOld()
            myTuple = RealData.getData(self.path, data)
            self.dataDict[data] = myTuple[1]
            self.timeDict[data] = time.time()

        return (data,self.dataDict[data])

    def removeOld(self) -> None:
        minimum = math.inf
        minumumKey = None
        for i in self.timeDict.keys():
            if self.timeDict[i] < minimum:
                minimum = self.timeDict[i]
                minimumKey = i
        
        del self.timeDict[minimumKey]
        del self.dataDict[minimumKey]
    
    def removeOutDated(self) -> None:
        removeTime = time.time()
        removing = []
        for i in self.timeDict.keys():
            if (removeTime - self.timeDict[i]) > self.TIME_LIMIT:
                removing.append(i)
                
        for i in removing:
            del self.dataDict[i]
            del self.timeDict[i]

    pass


class RealData():

    @staticmethod
    def getData(path, key) -> tuple:
        csv = pd.read_csv(path)
        for i in range(len(csv)):
            if csv["key"][i] == key:
                return (key, csv["value"][i])
        return ()
