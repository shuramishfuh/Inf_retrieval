from nltk.corpus import stopwords
import ReadFiles, JsonSer, json
import Iindex as InnvertedIndex
import functools, string, bisect, time
from colorama import Fore
import matplotlib.pyplot as plt


def convertOrAddToindex(wordsAndfileName, index):
    for wf in wordsAndfileName:
        print(Fore.YELLOW, "adding to index from ", wf[1])
        for word in wf[0]:
            if word in index:
                w = index[word]
                if wf[1] in w.getPosting():
                    w.setFrequency()
                else:
                    w.addPosting(str(wf[1]))
            else:
                index[word] = InnvertedIndex.Iindex(word, 1, str(wf[1]))


def changeFileNameToDocId(wordsAndfileName, docIds):
    for file in wordsAndfileName:
        print(Fore.CYAN, "changing file ", file[1])
        if file[1] in docIds.values():
            file[1] = docIds[file[1]]
        else:
            id = JsonSer.getDocId(6)
            docIds[id] = str(file[1])
            file[1] = id


def intersectUsingBinarySearch(postingOne, postingTwo):
    common = []
    if len(postingOne) < len(postingTwo):
        for posting in postingOne:
            index = bisect.bisect_left(postingTwo, posting)
            if postingTwo[index] == posting:
                common.append(posting)
    else:
        for posting in postingTwo:
            index = bisect.bisect_left(postingOne, posting)
            if postingOne[index] == posting:
                common.append(posting)
    if len(common) < 1:
        print("no common words")
        return -1
    else:
        return common


def IntersectUsingLinearSearch(postingOne, postingTwo):
    common = []
    if len(postingOne < len(postingTwo)):
        for posting in postingOne:
            if str(posting) in postingTwo:
                common.append(posting)
    else:
        for posting in postingTwo:
            if str(posting) in postingOne:
                common.append(posting)
    if len(common) < 1:
        print("no common words")
        return -1
    else:
        return common


print("started")
docIds = JsonSer.readDocId()
loadedIndex = JsonSer.readInvertedIndex("InvertedIndex.json")


def convertOrAddToindexSlower(wordsAndfileName, index):
    for wf in wordsAndfileName:
        for word in wf[0]:
            c = bisect.bisect_left(list(loadedIndex.keys()), word)
            if list(loadedIndex.keys())[c] == word:
                w = index[word]
                if wf[1] in w.getPosting():
                    w.setFrequency()
                else:
                    w.addPosting(str(wf[1]))
            else:
                index[word] = InnvertedIndex.Iindex(word, 1, str(wf[1]))




# print(len(loadedIndex))
#
# JsonSer.writeInvertedIndex(loadedIndex)
# JsonSer.writeDocId(docIds)
