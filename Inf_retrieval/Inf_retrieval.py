from nltk.corpus import stopwords  

import ReadFiles as ReadFiles

a ="testdata.txt"
b="dev.json"

#set up
path= ReadFiles.currentPath
files =ReadFiles.searchingAllFiles(path)
for file in files:
    print(file)
    words = ReadFiles.stopwordsRemove(file)
    wordsss= ReadFiles.stemWords(words)
    print(wordsss)
    text = input("prompt")



