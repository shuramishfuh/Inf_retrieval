import json
def to_json(obj):
    return json.dumps(obj, separators=(", ", ": "),indent = 4,  default=lambda obj: obj.__dict__)

def writeInvertedIndex(data):
    with open("InvertedIndex.json", "a") as write_file:
        json.dump((data), write_file, indent=4)

def readInvertedIndex():
    with open('InvertedIndex.json',"r") as f:
        d =f.read()
        return json.loads(d)