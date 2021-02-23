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
    for direc in currentPath.iterdir():
        if direc.is_dir() and direc.name == "stackoverflow":
            file = direc
        else:
            continue
    for dirpath, dirs, files in os.walk(file):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            file_list.append(pathlib.Path(fname))
    return file_list


# createBiWord combining every after word
def createBiWord(words, fileName):
    result = []
    for i in range(1, len(words) - 1, 2):
        temp = words[i - 1] + " " + words[i]
        result.append(temp)
    return result, pathlib.Path(fileName)


# read and remove stopwords
def readAndRemovestopwordsFromFile(fileName):
    file = open(str(fileName), "r", encoding="utf8", errors='ignore')
    read = file.read()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(read)
    filtered = []
    print(Fore.BLUE, "readAndRemovestopwordsFromFile from ", fileName)
    for word in word_tokens:
        if word not in stop_words and word.isalpha():
            filtered.append(word)
    return filtered, pathlib.Path(fileName)


# read and remove stopwords for positional index
def readAndRemovestopwordsFromFilePositional(fileName):
    file = open(str(fileName), "r", encoding="utf8", errors='ignore')
    read = file.read()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(read)
    filtered = []
    print(Fore.BLUE, "readAndRemovestopwordsFromFile from ", fileName)
    for idx, word in enumerate(word_tokens):
        if word not in stop_words and word.isalpha():
            filtered.append((word, idx))
    return filtered, pathlib.Path(fileName)


# stem words
def stemWords(words, fileName):
    snow_stemmer = SnowballStemmer(language='english')
    stem_words = []
    print(Fore.GREEN, "stopwords from ", fileName)
    for word in words:
        if len(word) != 1:
            stemmed = snow_stemmer.stem(word)
            stem_words.append(stemmed)
    stem_words = set(stem_words)
    return sorted(stem_words), pathlib.Path(fileName)


# stem words for positional
def stemWordsPositional(words, fileName):
    snow_stemmer = SnowballStemmer(language='english')
    stem_words = []
    print(Fore.GREEN, "stopwords from ", fileName)
    for word, idx in words:
        if len(word) != 1:
            stemmed = snow_stemmer.stem(word)
            stem_words.append((stemmed, idx))
    stem_words = set(stem_words)
    return sorted(stem_words), pathlib.Path(fileName)


# implement all read methods
def readAllBiWords():
    filesAndWords = []
    filesAndWordsBiWords = []
    files = searchingAllFiles()
    for file in files:
        w, f = readAndRemovestopwordsFromFile(file)
        words, fileName = stemWords(w, f)
        filesAndWords.append([words, fileName])
    # convert to biWord
    for wfs in filesAndWords:
        xwords, yfileName = createBiWord(wfs[0], wfs[1])
        filesAndWordsBiWords.append([xwords, yfileName])
    return filesAndWordsBiWords


def readAll():
    filesAndWords = []
    filesAndWordsBiWords = []
    files = searchingAllFiles()
    for file in files:
        w, f = readAndRemovestopwordsFromFile(file)
        words, fileName = stemWords(w, f)
        filesAndWords.append([words, fileName])
    return filesAndWords


def readAllPositional():
    filesAndWords = []
    filesAndWordsBiWords = []
    files = searchingAllFiles()
    for file in files:
            w, f = readAndRemovestopwordsFromFilePositional(file)
            words, fileName = stemWordsPositional(w, f)
            filesAndWords.append([words, fileName])
    # convert to biWord

    return filesAndWords
