from nltk.corpus import stopwords  
import ReadFiles, JsonSer
import Iindex as InnvertedIndex


#set up
#path= ReadFiles.currentPath                
def ReadAll(path=ReadFiles.currentPath):
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
    
a = InnvertedIndex.Iindex("cool",2,"doc1")
a.addPosting("nah")
a.addPosting("colour")
a.addPosting("fine")
b= JsonSer.to_json(a)
print(vars(a))
JsonSer.writeInvertedIndex(vars(a))

#c = InnvertedIndex.Iindex("fdfd",4,"fdf")
#c.addPosting("f")
#c.addPosting("f")
#c.addPosting("f")
#d=JsonSer.to_json(c)
#JsonSer.writeInvertedIndex(d)

#LoadedIndex = JsonSer.readInvertedIndex()
#print((LoadedIndex))

