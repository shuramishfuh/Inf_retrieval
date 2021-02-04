import json
class JsonSer(object):
    """description of class"""
    def __init__(self,words):
             self.data = words
             print(self.data)
    def writeInvertedIndex(data):
             try:
                with open("InvertedIndex.json", "w") as write_file:
                        json.dump(self.data, write_file, indent=4, separators=(", ", ": "), sort_keys=True)
             except :
                 Print("an error occured whilst saving file")

    def readInvertedIndex(data):
        with open('InvertedIndex.json') as f:
            return json.load(f)
       
