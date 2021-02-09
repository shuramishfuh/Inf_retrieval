from nltk.corpus import stopwords  
import ReadFiles, JsonSer, json
import Iindex as InnvertedIndex
import functools, string, bisect, time 
import matplotlib.pyplot as plt


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


print("***********************************************************************")
print("***************************data 1******************************")
print(" number of distinct words is :",len(loadedIndex.keys()))
print(" number of documents :",len(docIds))
for i in docIds:
    b = list(filter(lambda x: i in x.getPosting(),loadedIndex.values()))
    print("average number of distinct words in",i ,"is",len(b))

print("size of index is 15% of all files")
print("***********************************************************************")
print("***************************data 1 Ends******************************")


#***********************************************************************

alpha =list(string.ascii_lowercase)
letterDocIds={}
for x in alpha:
    subList =[]
    for u,y in loadedIndex.items():
        if(str(u).startswith(x)):
            for  w in y.getPosting():
              if w not in subList:
                subList.append(w)
    letterDocIds[x]=subList
with open("queries/StartsWithletterAndDocId.txt", "w") as write_file:
        json.dump(letterDocIds , write_file, indent=4)
#***********************************************************************




#***********************************************************************
def convertOrAddToindexSlower(wordsAndfileName,index):
    for wf in wordsAndfileName:
       for word in wf[0]:
         c = bisect.bisect_left(list(loadedIndex.keys()),word)
         if list(loadedIndex.keys())[c] == word :
            w = index[word]
            if( wf[1] in w.getPosting()):
                w.setFrequency()
            else:
                w.addPosting(str(wf[1]))
         else:
                  index[word] = InnvertedIndex.Iindex(word,1,str(wf[1]))

#***********************************************************************

######################################
#wrds =[]
#freq=[]
#for wrd,pst in loadedIndex.items():
#    wrds.append(wrd)
#    freq.append(pst.getFrequency())

#plt.bar(wrds,freq,align='center') # A bar chart
#plt.xlabel('Bins')
#plt.ylabel('Frequency')
#for i in range(len(wrd)):
#    plt.hlines(wrds[i],0,freq[i]) # Here you are drawing the horizontal lines
#plt.show()


# normal 
#start1 = time.time()
#convertOrAddToindex(wordsAndfileName,loadedIndex)
#end1 = time.time()
#start = time.time()
#convertOrAddToindexSlower(wordsAndfileName,loadedIndex)
#end = time.time()
#faster =end1 - start1
#slower=end - start
#print("time for both is :",slower," for slower algorithm and",faster,"for faster algorithm")

JsonSer.writeInvertedIndex(loadedIndex) 
JsonSer.writeDocId(docIds)


#***********************************************************************
#   Queries

#a =list(filter(lambda x:x.getWord() =="after" ,list(loadedIndex.values()))) # find words
#b =list(filter(lambda x:x.getWord() =="after" or x.getWord() =="also",list(loadedIndex.values()))) # find words
#c =list(filter(lambda x:x.getWord() =="after"  and not x.getWord() =="after",list(loadedIndex.values()))) # should return nothing 
#d =list(filter(lambda x:x.getWord() =="after"  and  x.getWord() =="advertis",list(loadedIndex.values()))) 
#e =list(filter(lambda x:x.getPosting() !=""  list(loadedIndex.values()))) 

#for ui in a:
#    print(ui.getPosting())
  