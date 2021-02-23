import bisect
import ReadFiles as Read
from colorama import Fore

import Iindex as InnvertedIndex
import JsonSer


def convertOrAddToindex(innerwordsAndfileName, index):
    for wf in innerwordsAndfileName:
        print(Fore.YELLOW, "adding to index from ", wf[1])
        for x_word in wf[0]:
            if x_word in index:
                w = index[x_word]
                if wf[1] in w.getPosting():
                    w.setFrequency()
                else:
                    w.addPosting(str(wf[1]))
            else:
                index[x_word] = InnvertedIndex.Iindex(x_word, 1, str(wf[1]))


def convertOrAddToindexPositionalIndex(innerwordsAndfileName, index):
    for wf in innerwordsAndfileName:
        print(Fore.YELLOW, "adding to index from ", wf[1])
        for x_word, position in wf[0]:
            if x_word in index:
                w = index[x_word]
                pos = w.getPosting()
                if wf[1] in pos:
                    w.addPostingAlreadyExistWord(wf[1], position)
                else:
                    w.addPosting(str(wf[1]), position)
            else:
                index[x_word] = InnvertedIndex.PositionalIndex(x_word, str(wf[1]), position)


def changeFileNameToDocId(innerwordsAndfileName, interenalDocIds):
    for file in innerwordsAndfileName:
        print(Fore.CYAN, "changing file ", file[1])
        if not file[1] in interenalDocIds.values():
            fileId = JsonSer.getDocId(8)
            interenalDocIds[fileId] = str(file[1])
            file[1] = fileId


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


def intersectSingleUsingBinary(y_word, index):
    result = (bisect.bisect_left(index, y_word))
    if index[result] == y_word:
        return "NOne"
    else:
        return result


def convertOrAddToindexSlower(innerwordsAndfileName, index):
    for wf in innerwordsAndfileName:
        for x_word in wf[0]:
            c = bisect.bisect_left(list(index.keys()), x_word)
            if list(index.keys())[c] == x_word:
                w = index[x_word]
                if wf[1] in w.getPosting():
                    w.setFrequency()
                else:
                    w.addPosting(str(wf[1]))
            else:
                index[x_word] = InnvertedIndex.Iindex(x_word, 1, str(wf[1]))


# driver for regular index
# Read and build index
# print("started")
# docIds = JsonSer.readDocId()
# loadedIndex = JsonSer.readInvertedIndex("InvertedIndex.json")

# wordsAndfileName = ReadFiles.readAll()
# changeFileNameToDocId(wordsAndfileName, docIds)
# convertOrAddToindex(wordsAndfileName, loadedIndex)
# JsonSer.writeInvertedIndex(loadedIndex)
# JsonSer.writeDocId(docIds)
# print(len(loadedIndex))

# word = " reflect regular"
# b =intersectSingleUsingBinary(word, list(loadedIndex.keys()))
# print(type(b))
# print(loadedIndex["reflect regular"])


# driver for positional index
positionalWords = Read.readAllPositional()
# docIds = JsonSer.readDocIdPositional()
# loadedIndex = JsonSer.readInvertedIndexPositional("DocIdPositional.json")
loadedIndex={}
docIds={}
changeFileNameToDocId(positionalWords, docIds)
convertOrAddToindexPositionalIndex(positionalWords, loadedIndex)
JsonSer.writeInvertedIndexPositional(loadedIndex)
JsonSer.writeDocIdPositional(docIds)
# print(loadedIndex)
