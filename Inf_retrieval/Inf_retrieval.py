from nltk.corpus import stopwords  
import ReadFiles, JsonSer, json
import Iindex as InnvertedIndex


loadedIndex = JsonSer.readInvertedIndex("InvertedIndex.json")            

wordsAndfileName = ReadFiles.readAll()

def convertOrAddToindex(wordsAndfileName,index):
    for wf in wordsAndfileName:
       for word in wf[0]:
         if (word in index):
           w = index[word]
           if( wf[1] in w.getPosting()):
                w.setFrequency()
           else:
                w.addPosting(str(wf[1]))
         else:
                  index[word] = InnvertedIndex.Iindex(word,1,str(wf[1]))




convertOrAddToindex(wordsAndfileName,loadedIndex)
print(loadedIndex)

JsonSer.writeInvertedIndex(loadedIndex) 








#a = InnvertedIndex.Iindex("ipooy2",2,"doc1")
#a.addPosting("cdfdo")
#a.addPosting("ffdgf")
#a.addPosting("weseew")
#loadedIndex[a.getWord()]=a
#JsonSer.writeInvertedIndex(loadedIndex) 

