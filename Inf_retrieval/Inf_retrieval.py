from nltk.corpus import stopwords  
import ReadFiles, JsonSer, json
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
    
#a = InnvertedIndex.Iindex("cool",2,"doc1")
#a.addPosting("nah")
#a.addPosting("colour")
#a.addPosting("fine")

#c = InnvertedIndex.Iindex("fdfd",4,"fdf")
#c.addPosting("f")
#c.addPosting("f")
#c.addPosting("f")
#u ={}
#u
#JsonSer.writeInvertedIndex(u) 

#def AddTodict(data):
    

LoadedIndex = JsonSer.readInvertedIndex()
print((LoadedIndex))

