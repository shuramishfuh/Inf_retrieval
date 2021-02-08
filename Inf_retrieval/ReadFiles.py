import  pathlib,bisect
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize 

Filepaths = pathlib.Path(__file__).parent

# read files from data folder
def searchingAllFiles(currentPath=Filepaths):  
    file_list = []

    for file in currentPath.iterdir():
        if file.is_file():
            p = pathlib.Path(file)
            if  (str(file).endswith(".json")) and (p.name !="InvertedIndex.json"):
               file_list.append(file)
        else:
            file_list.extend(searchingAllFiles(currentPath/file))

    return file_list


# read and remov stopwords
def readAndRemovestopwords(fileName):
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
    return sorted(stem_words),fileName

def readAll():
    filesAndWords =[]
    files =searchingAllFiles()
    for file in files:
            w,f =readAndRemovestopwords(file)
            words,fileName =stemWords(w,f)
            filesAndWords.append([words,fileName])
    return filesAndWords

