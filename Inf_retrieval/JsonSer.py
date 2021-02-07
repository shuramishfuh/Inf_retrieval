import json, os,Iindex
from operator import attrgetter

def writeInvertedIndex(data):
    with open("InvertedIndex.json", "w+") as write_file:
        json.dump( fromClassToDic(data), write_file, indent=4)

def readInvertedIndex(file): # returns list of dic
   if os.stat(file).st_size != 0:
        with open(file,"r") as file:
            data =json.load(file)
            data =sorted(data, key= lambda index :index['_Iindex__word'])
            return fromDicToClass(data)
   else: 
       index={}
       return index

# convert from Dic To to
def fromDicToClass(dataset):
    index=[]
    dicIndex ={}
    for data in  dataset:
           a =Iindex.Iindex(data["_Iindex__word"],data["_Iindex__frequency"],data["_Iindex__postingList"])
           index.append(a)
    for x in index:
     dicIndex[x.getWord()]=x
    return dicIndex


# convert from Class To Dic
def fromClassToDic(dataset):
    index=[]
    for data in  dataset:
           a =vars(data)
           index.append(a)
    return index

def builtDic(word,index):
    outIndexDic = dict[word]=index
    return outIndexDic