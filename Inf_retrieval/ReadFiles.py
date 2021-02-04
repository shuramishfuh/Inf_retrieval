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
    filtered = [w for w in word_tokens if not w in stop_words]  
    filtered = []  
  
    for w in word_tokens:  
        if w not in stop_words:  
            filtered.append(w)  
    return filtered 


#stem words
def stemWords(words):
    snow_stemmer = SnowballStemmer(language='english') 
    stem_words =[]
    for word in words:
         stemmed = snow_stemmer.stem(word) 
         stem_words.append(stemmed) 
    return stem_words