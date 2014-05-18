import pickle
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
trainDir = "/Users/maxluyifan/Desktop/data/train"


def getWordsFromOneFile ( fileName ):
	f = open ( fileName , "r" )
	line = f.read()
	wordList = line.split (" ")
        return wordList

trainPath = sys.argv [ 1 ] ;
wordMap = {} ;
wordDict = {} ;
documentId = -1 ;
documentDict ={} ;
wordId = -1 ;
trainFileClassList = os.listdir ( trainPath ) ;
for  trainFileClass in trainFileClassList:
    trainFileList = os.listdir (  trainPath + "/" + trainFileClass ) ;
    for trainFile in trainFileList:
        trainFilePath = trainPath + "/" + trainFileClass + "/" + trainFile ;
        wordList = getWordsFromOneFile ( trainFilePath ) ;
        documentId += 1
        documentDict [ documentId ] ={} ;
        documentDict [ documentId ][ "totalWords" ] = 0 ;
        documentDict [ documentId ][ "words" ] = {}
        for word in wordList:
            if  word in wordMap:
                thisWordId = wordMap [ word ]
                if wordDict [ thisWordId ][ "lastFile" ] != trainFilePath:
                    wordDict [ thisWordId ][ "lastFile" ] = trainFilePath
                    wordDict [ thisWordId ][ "documents" ] += 1
                    documentDict [ documentId ][ "words" ][ thisWordId ] = 1
                else:
                    documentDict [ documentId ][ "words" ][ thisWordId ] = +1
            else:
                wordId += 1
                wordMap [ word ] = wordId
                wordDict [ wordId ] ={}
                wordDict [ wordId ]["lastFile" ] = trainFilePath
                wordDict [ wordId ]["documents"] = 1
                documentDict [ documentId ][ "words" ][ wordId ] = 1
            documentDict [ documentId ][ "totalWords" ] += 1





with open ( "/Users/maxluyifan/Desktop/documentDict.pickle" , "wb" ) as picklefile:
    pickle.dump ( documentDict , picklefile )
    picklefile.close ( );




