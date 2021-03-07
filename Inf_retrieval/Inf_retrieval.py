import bisect
import time
from functools import wraps
from itertools import product
import enchant

from colorama import Fore

import Iindex as InnvertedIndex
import JsonSer


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("time Taken for ", func.__name__, " is ", end - begin)
        return result

    return inner()


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


def generateAllPossibleBiWords(phraseIn):
    strings = []
    phrase = []
    for string in phraseIn.split(" "):
        strings.append(string)
    for i in range(len(strings) - 1):
        phrase.append(strings[i] + " " + strings[i + 1])
    return phrase


def easySearch(phrase, index):
    if phrase in index.keys():
        return index[phrase]


def FindDocsCommonTOPhrase(phrase, index):
    allList = []
    for x in index:
        allList.append(x.getPosting())
    return list(set.intersection(*map(set, allList)))


def searchAllWordsReturnListOfIndex(words, index):
    result = []
    for word in words.split():
        temp = easySearch(word, index)
        if temp:
            result.append(temp)
    return result


def intersectToProduceContainingDoc(phrase, index):
    match = []
    for phrase_word in generateAllPossibleBiWords(phrase):
        out = easySearch(phrase_word, index)
        if out:
            match.append(out)
    output = ""
    if match:
        output = FindDocsCommonTOPhrase(phrase, match)
    return output


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


# takes returned index of two index
def intersectPositional(ReturnedIndex):
    # get name
    first = set(ReturnedIndex[0].getPosting())
    second = set(ReturnedIndex[1].getPosting())
    intersect = list(first.intersection(second))
    intersect.sort()
    # get elements
    firstPosting = ReturnedIndex[0].getPosting()
    secondPosting = ReturnedIndex[1].getPosting()
    common = []
    for docId in intersect:  # order might change test forward and backward
        if len(firstPosting[docId]) < len(secondPosting[docId]):
            for pos in firstPosting[docId]:
                if ((pos + 1) in secondPosting[docId]) or (pos - 1) in secondPosting[docId]:
                    common.append(docId)
        else:
            for pos in secondPosting[docId]:
                if ((pos + 1) in firstPosting[docId]) or (pos - 1) in firstPosting[docId]:
                    common.append(docId)
    return common


def generateAllPossibleWords(word):
    d = enchant.Dict("en_US")
    d.check(word)
    return d.suggest(word)


def returnEditDistance(word, testString):
    return enchant.utils.levenshtein(word, testString)


def getWordsOfEditDistanceTwo(word):
    a = generateAllPossibleWords(word)
    out = []
    for x in a:
        if returnEditDistance(word, x) < 3:
            out.append(x)
    return out


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


# driver for BiwordIndex
# loadedIndex = JsonSer.readInvertedIndex("InvertedIndex.json")
# docIds = JsonSer.readDocId()

# d = easySearch(word4,loadedIndex)
# print(d.getPosting())
# c = " last lastact inner input french from"
# start = time.time()
# a = (intersectToProduceContainingDoc(c, loadedIndex))
# end = time.time()
# print(end - start)

# end


# driver for positional index

# positionalWords = Read.readAllPositional()
# docIds = JsonSer.readDocIdPositional()
# loadedIndex = JsonSer.readInvertedIndexPositional("DocIdPositional.json")
# changeFileNameToDocId(positionalWords, docIds)
# convertOrAddToindexPositionalIndex(positionalWords, loadedIndex)
# JsonSer.writeInvertedIndexPositional(loadedIndex)
# JsonSer.writeDocIdPositional(docIds)
# print(loadedIndex)

# a = "to be"
# c = " last lastact inner input french from"
# #
# loadedIndex = JsonSer.readInvertedIndexPositional("InvertedIndexPositional.json")
# start = time.time()
# d = searchAllWordsReturnListOfIndex(c, loadedIndex)
# intersectPositional(d)
# end = time.time()
# print(end - start)


