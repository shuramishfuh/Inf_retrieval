import  pathlib
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize 

currentPath = pathlib.Path(__file__).parent

# read files from data folder
def searchingAllFiles(currentPath):  
    file_list = []

    for file in currentPath.iterdir():
        if file.is_file():
            if  (str(file).endswith(".json")):
               file_list.append(file)
        else:
            file_list.extend(searchingAllFiles(currentPath/file))

    return file_list


# read and remov stopwords
def stopwordsRemove(fileName):
    file = open(str(fileName),"r" ,encoding="utf8") 
    example_sent =  file.read()
    stop_words = set(stopwords.words('english'))  
    word_tokens = word_tokenize(example_sent)  
    filtered = [word for word in word_tokens if not word in stop_words]  
    filtered = []  
  
    for word in word_tokens:  
        if word not in stop_words and word.isalpha():  
            filtered.append(word)  
    return filtered ,fileName


#stem words
def stemWords(words,fileName):
    snow_stemmer = SnowballStemmer(language='english') 
    stem_words =[]
    for word in words:
         stemmed = snow_stemmer.stem(word) 
         stem_words.append(stemmed) 
    return stem_words,fileName


def addToIndex(index,words,fileName):
    for word in words:  
        if word not in stop_words and word.isalpha():  
            filtered.append(word)  
    return filtered 


