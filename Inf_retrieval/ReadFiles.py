import pathlib
import os
from colorama import Fore
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

Filepaths = pathlib.Path(__file__).parent


# read files from data folder
def searchingAllFiles(currentPath=Filepaths):
    file_list = []
    file = pathlib.Path
    for dir in currentPath.iterdir():
        if dir.is_dir() and dir.name == "stackoverflow":
            file = dir
        else:
            continue
    for dirpath, dirs, files in os.walk(file):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            file_list.append(pathlib.Path(fname))
    return file_list


# read and remove stopwords
def readAndRemovestopwordsFromFile(fileName):
    file = open(str(fileName), "r", encoding="utf8",errors='ignore')
    read = file.read()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(read)
    filtered = []
    print( Fore.BLUE,"readAndRemovestopwordsFromFile from ", fileName)
    for word in word_tokens:
        if word not in stop_words and word.isalpha():
            filtered.append(word)
    return filtered, pathlib.Path(fileName)


def stemWords(words, fileName):
    snow_stemmer = SnowballStemmer(language='english')
    stem_words = []
    print(Fore.GREEN,"stopwords from ", fileName)
    for word in words:
        if len(word) != 1:
            stemmed = snow_stemmer.stem(word)
            stem_words.append(stemmed)
    stem_words = set(stem_words)
    return sorted(stem_words), pathlib.Path(fileName)


def readAll():
    filesAndWords = []
    files = searchingAllFiles()
    for file in files:
        w, f = readAndRemovestopwordsFromFile(file)
        words, fileName = stemWords(w, f)
        filesAndWords.append([words, fileName])
    return filesAndWords



