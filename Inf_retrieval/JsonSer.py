import json
def to_json(obj):
    return json.dumps(obj, separators=(", ", ": "),  default=lambda obj: obj.__dict__)

def writeInvertedIndex(data):
    with open("InvertedIndex.json", "w") as write_file:
        json.dump(data, write_file )

def readInvertedIndex():
    with open('InvertedIndex.json') as f:
        return json.load(f)
       
