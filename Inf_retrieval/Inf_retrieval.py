from nltk.corpus import stopwords  
import ReadFiles, JsonSer
import Iindex as InnvertedIndex


#set up
#path= ReadFiles.currentPath
#files =ReadFiles.searchingAllFiles(path)
#for file in files:
#    print(file)
#    words = ReadFiles.stopwordsRemove(file)
#    stemWordss= ReadFiles.stemWords(words)
#    stemWordss.sort()
    
a = InnvertedIndex.Iindex("cool",2,"doc1")
a.addPosting("nah")
a.addPosting("colour")
a.addPosting("fine")


