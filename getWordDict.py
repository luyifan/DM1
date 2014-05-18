import pickle
import sys
import os
reload ( sys )
sys.setdefaultencoding('utf-8')

def getWordsFromOneFile ( filename ):
    f = open ( filename , "r" )
    wordList = f.read().split(" ")
    return wordList

def getAbsolutePath ( basePath , filename ):
    return basePath + "/" + filename

def getWordDictFromDir( trainPath ):
    wordDict = {} ;
    totalDocuments = 0 ;
    trainFileClassList = os.listdir ( trainPath )
    for trainFileClass in trainFileClassList:
        trainFileClassDir = getAbsolutePath ( trainPath , trainFileClass )
        trainFileList = os.listdir ( trainFileClassDir )
        for trainFile in trainFileList:
            filename = getAbsolutePath( trainFileClassDir , trainFile )
            totalDocuments += 1
            wordList = getWordsFromOneFile( filename )
            for word  in wordList:
                if word in wordDict:
                    if filename != wordDict [ word ][ "lastFile" ]:
                        wordDict [ word ][ "timesInDocuments" ] += 1
                        wordDict [ word ][ "lastFile" ] = filename
                else:
                    wordDict [ word ] ={};
                    wordDict [ word ][ "lastFile" ] = filename
                    wordDict [ word ][ "timesInDocuments" ] = 1
    return ( totalDocuments , wordDict )
if __name__ == "__main__":
    textPath = sys.argv [ 1 ]
    trainPath = getAbsolutePath ( textPath , "train" )
    ( totalDocuments , wordDict ) = getWordDictFromDir ( trainPath )
    wordPickleDict = {} ;
    wordPickleDict[ "totalDocuments" ] = totalDocuments
    wordPickleDict[ "words" ] = {}
    for word in wordDict:
        wordPickleDict [ "words" ][ word ] = wordDict [ word ][ "timesInDocuments" ]
    wordDictFilename = getAbsolutePath ( textPath , "store/wordDict.pickle" )
    with open ( wordDictFilename , "wb" ) as picklefile:
        pickle.dump ( wordPickleDict , picklefile )
        picklefile.close()
'''    ftest = open ( "/Users/maxluyifan/Desktop/test.txt" , "w")
    for word in wordDict:
        ftest.write ( word )
        ftest.write ( " " )
        ftest.write ( wordDict [ word ][ "lastFile" ] )
        ftest.write ( " " )
        ftest.write ( str(wordDict [ word ][ "timesInDocuments" ]))
        ftest.write ( "\n" )
'''
