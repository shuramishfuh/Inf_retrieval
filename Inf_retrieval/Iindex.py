class Iindex(object):
    """contains inverted index structure"""

    def __init__(self, word, frequency, docId):
        self.__word = word
        self.__frequency = frequency
        self.__postingList = []
        if type(docId) == list:
            self.__postingList += docId
        else:
            self.__postingList.append(docId)

    def addPosting(self, docId):
        self.__postingList.append(docId)
        self.__frequency += 1

    def getWord(self):
        return self.__word

    def getFrequency(self):
        return self.__frequency

    def setFrequency(self):
        self.__frequency += 1

    def getPosting(self):
        return self.__postingList


class PositionalIndex(object):

    def __init__(self, *args):
        if len(args) > 2:
            self.__word = args[0]
            self.__postingList = {args[1]: args[2]}
            self
        else:
            self.__word = args[0]
            self.__postingList = args[1]

    def addPostingAlreadyExistWord(self, docId, position):
        temp = self.__postingList[docId]
        temp.append(position)
        self.__postingList[docId] = temp

    def addPosition(self, docId, position):
        return self.__postingList[{docId: position}]

    def getPosting(self):
        return self.__postingList

    def getWord(self):
        return self.__word
