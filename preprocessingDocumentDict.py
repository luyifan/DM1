import pickle
import os
import sys
from getWordDict import getWordsFromOneFile
from getWordDict import getAbsolutePath
reload ( sys )
sys.setdefaultencoding ( 'utf-8' )

def getWordMap ( filename ):
    with open ( filename , "rb" ) as picklefile:
        wordMap = pickle.load ( picklefile )
        picklefile.close ( )
    return wordMap
def getOneDocumentList ( filename , wordMap ):
    wordList = getWordsFromOneFile ( filename )
    oneDocumentList = [];
    for word in wordList:
        if word in wordMap:
            wordId = wordMap [ word ]
            if not ( wordId in oneDocumentList ):
                oneDocumentList.append (  wordId )
        else:
            pass
            #not in the word map
    return oneDocumentList

def getDocumentDictFromDir ( trainPath , wordMap ):
    documentDict = {}
    documentId = -1
    trainFileClassList = os.listdir ( trainPath )
    for trainFileClass in trainFileClassList:
        trainFileClassDir = getAbsolutePath ( trainPath , trainFileClass )
        trainFileList = os.listdir ( trainFileClassDir )
        for trainFile in trainFileList:
            filename = getAbsolutePath ( trainFileClassDir , trainFile )
            documentId += 1
            documentDict [ documentId ] = {}
            documentDict [ documentId ][ "words" ] = getOneDocumentList ( filename , wordMap )
            documentDict [ documentId ][ "classLabel" ] = int ( trainFileClass )
    return documentDict

def storeDocumentDict ( filename , documentDict ):
    with open (  filename , "wb" ) as picklefile:
        pickle.dump (  documentDict , picklefile )
        picklefile.close ( )
if __name__ == "__main__":
    textPath = sys.argv [ 1 ]
    trainPath = getAbsolutePath ( textPath , "train" )
    wordMapFilename = getAbsolutePath ( textPath , "store/wordDictByThreshold.pickle" )
    wordMap = getWordMap ( wordMapFilename )
    #print wordMap
    documentDict = getDocumentDictFromDir ( trainPath , wordMap )
    documentDictPickleFilename = getAbsolutePath ( textPath , "store/documentDict.pickle" )
    storeDocumentDict ( documentDictPickleFilename , documentDict )
