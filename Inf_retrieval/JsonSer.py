import json
import Iindex

def writeInvertedIndex(data):
    with open("InvertedIndex.json", "a") as write_file:
        json.dump( vars(data), write_file, indent=4)

def readInvertedIndex(): # returns list of dic
    with open('InvertedIndex.json',"r") as file:
       index=[]
       for data in  json.load(file):
           a =Iindex.Iindex(data["_Iindex__word"],data["_Iindex__frequency"],data["_Iindex__postingList"])
           index.append(a)
    return index

       