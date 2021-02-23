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

    def __init__(self, word, docId, position):
        self.__word = word
        self.__postingList = {docId: [position]}
        set(self.__postingList)

    def __init__(self, word, postings):
        self.__word = word
        self.__postingList = postings

    def addPosting(self, docId, position):
        self.__postingList[docId] = [position]
        return self

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
