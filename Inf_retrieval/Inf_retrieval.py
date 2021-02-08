from nltk.corpus import stopwords  
import ReadFiles, JsonSer, json
import Iindex as InnvertedIndex


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

def changeFileNameToDocId(wordsAndfileName,docIds):
     for file in wordsAndfileName:
        if(file[1] in docIds.values()):
           file[1]=docId[file[1]]
        else:
            id =JsonSer.getDocId(6)
            docIds[id]=str(file[1])
            file[1]=id



docIds =JsonSer.readDocId()
loadedIndex = JsonSer.readInvertedIndex("InvertedIndex.json")            

wordsAndfileName = ReadFiles.readAll()
changeFileNameToDocId(wordsAndfileName,docIds)


convertOrAddToindex(wordsAndfileName,loadedIndex)



#JsonSer.writeInvertedIndex(loadedIndex) 
#JsonSer.writeDocId(docIds)
