import json, os,Iindex, operator,random,string
from operator import attrgetter
from functools import reduce

def writeInvertedIndex(data):
    with open("InvertedIndex.json", "w") as write_file:
        json.dump( fromClassToDic(data), write_file, indent=4)

def readInvertedIndex(file): # returns list of dic
   if os.stat(file).st_size != 0:
        with open(file,"r") as file:
            data =json.load(file)
            data =sorted(data, key= lambda index :index['_Iindex__word'])
            return fromDicToClass(data)
   else: 
       index={}
       print("Inverted index is empty ")
       return index

# convert from Dic To to
def fromDicToClass(dataset):
    dicIndex ={}
    for data in  dataset:   
           x =Iindex.Iindex(data["_Iindex__word"],data["_Iindex__frequency"],list(map(lambda x: x ,data["_Iindex__postingList"])))
           c= dicIndex[x.getWord()]=x
    return dicIndex


# convert from Class To Dic
def fromClassToDic(dataset):
  return list(map(lambda x: vars(x),dataset.values()))





#from file to docId

            
#from file to docId
def changeDocIdToFileName(id,DocIds):
    
        if(id in DocIds):
           return DocIds[id]
        else:
            return ""
       

#generate docId
def getDocId(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def writeDocId(data):
    with open("DocId.json", "w") as write_file:
         json.dump( data, write_file, indent=4)

def readDocId():
    if os.stat("DocId.json").st_size != 0:
        with open("DocId.json", "r") as read_file:
            data =json.load(read_file)
            return data
    else:
            dic ={}
            return dic