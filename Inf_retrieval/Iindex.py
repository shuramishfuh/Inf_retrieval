class Iindex(object):
    """contains inverted index structure"""
    def __init__(self, word, frequency,docId):
        self.__word = word  
        self.__frequency = frequency 
        self.__postingList=[]
        if(type(docId) == list):
         self.__postingList+= docId
        else: 
            self.__postingList.append(docId)

    def addPosting(self, docId):
        self.__postingList.append(docId)
        self.__frequency += 1
       
    def getWord(self):
        return self.__word 
    
    def getFrequency(self):
        return self.__frequency

    def getPosting(self ):
        return self.__postingList

   
