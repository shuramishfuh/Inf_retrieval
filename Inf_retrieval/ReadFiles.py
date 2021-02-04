import  pathlib
from nltk.corpus import stopwords  

currentPath = pathlib.Path(__file__).parent

# read files from data folder
def searching_all_files(currentPath):  
    file_list = []

    for file in currentPath.iterdir():
        if file.is_file():
            if  (str(file).endswith(".json")):
               file_list.append(file)
        else:
            file_list.extend(searching_all_files(currentPath/file))

    return file_list
files = searching_all_files(currentPath)

# read and normalize words using stopwords
def read_content_and_Normalize(fileNames):
    stop_words = set(stopwords.words('english')) 
    for doc in fileNames:
        file = open(doc,"r+",encoding="utf8",errors='ignore') 
        content= file.read()
        words = content.split()    
        for word in words: 
            if word not in stop_words:
              file = open(doc,"w",encoding="utf8",errors='ignore') 
              file.write(word)  
    file.close()
    return  None

read_content_and_Normalize(files)