from nltk.corpus import stopwords  
import ReadFiles, JsonSer, json,bisect, functools
import Iindex as InnvertedIndex


#set up
#path= ReadFiles.currentPath                
def ReadAll(path=ReadFiles.Filepaths):
    files =ReadFiles.searchingAllFiles(path)
    for file in files:
        print(file)
        words = ReadFiles.stopwordsRemove(file)
        stemWordss= ReadFiles.stemWords(words)
        stemWordss.sort()

def listIt(invertedIndex, doc, sWords):  # write binary search
    for word in sWord:
        if word in invertedIndex:
            pass
    

def addToIndex(index,words,fileName):
    for word in words:  
        if (bisect.bisect_left(index,word)):  
            filtered.append(word)  
    return filtered 
loadedIndex = JsonSer.readInvertedIndex("InvertedIndex.json")
for i in loadedIndex.values():
    print(i.getPosting())
#for i in loadedIndex.values():
#    print(i.getPosting())
#a = ReadFiles.searchingAllFiles(ReadFiles.Filepaths)
#b = ReadFiles.readAndRemovestopwords(a[1])
#c=ReadFiles.stemWords(b[0],b[1])

#c =ReadFiles.readAll()
#print(c[0][1])


a = InnvertedIndex.Iindex("ioy2",2,"doc1")
a.addPosting("cdfdo")
a.addPosting("ffdgf")
a.addPosting("weseew")
loadedIndex[a.getWord()]=a
JsonSer.writeInvertedIndex(loadedIndex) 

