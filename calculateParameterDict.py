import sys
import os
import pickle
from getWordDict import getAbsolutePath
reload ( sys )
sys.setdefaultencoding ( 'utf-8' )


def loadDocumentDict ( filename ):
    with open ( filename , "rb" ) as documentPickleFile:
        documentDict = pickle.load( documentPickleFile )
        documentPickleFile.close ()
    return documentDict

def loadWordMap ( filename ):
    with open ( filename , "rb" ) as wordPickleFile:
        wordMap = pickle.load ( wordPickleFile )
        wordPickleFile.close()
    return wordMap
def getTotalWordsFromMap ( wordMap ):
    totalWords = -1
    for word in wordMap:
        if  wordMap [ word ] > totalWords:
            totalWords = wordMap [ word ]
    return totalWords

def getClassLabelListFromDocumentDict ( documentDict ):
    classLabelList =[]
    for documentId in documentDict:
        if not ( documentDict [ documentId ][ "classLabel" ] in classLabelList ):
            classLabelList.append ( documentDict [ documentId ][ "classLabel" ] )
    return classLabelList ;
def calculateParameter (  documentDict , totalWords , classLabelList ):
    parameterDict = {}
    parameterDict [ "prior" ] = {}
    parameterDict [ "maxwordlikelihood" ] = {}
    for classLabel in classLabelList:
        parameterDict [ "maxwordlikelihood" ][ classLabel ] = {}
        for wordId in range ( 0 , totalWords + 1):
            parameterDict [ "maxwordlikelihood" ][ classLabel ][ wordId ] = 1
    totalDocument = 0
    for classLabel in classLabelList:
        parameterDict [ "prior" ][ classLabel ] = 0
        for documentId in documentDict:
            if documentDict [ documentId ][ "classLabel" ] == classLabel:
                for wordId in documentDict [ documentId ][ "words" ]:
                    parameterDict [ "maxwordlikelihood" ][ classLabel ][ wordId ] += 1
                parameterDict [ "prior" ][ classLabel ] += 1
                totalDocument += 1
        for wordId in parameterDict [ "maxwordlikelihood" ][ classLabel ]:
            parameterDict [ "maxwordlikelihood" ][ classLabel ][ wordId ] /= float ( parameterDict [ "prior" ][ classLabel ] + totalWords )
    for classLabel in classLabelList:
        parameterDict [ "prior" ][ classLabel ] /= float ( totalDocument )
    return parameterDict
def storeParameterDict ( filename , parameterDict ):
    with open ( filename , "wb" ) as parameterPickleFile:
        pickle.dump( parameterDict , parameterPickleFile )
        parameterPickleFile.close ()

if __name__ == "__main__":
    textPath = sys.argv [ 1 ]
    wordPickleFilename = getAbsolutePath  ( textPath ,  "store/wordDictByThreshold.pickle"  )
    wordMap = loadWordMap ( wordPickleFilename )
    documentPickleFilename = getAbsolutePath ( textPath , "store/documentDict.pickle" )
    documentDict = loadDocumentDict ( documentPickleFilename )
    totalWords = getTotalWordsFromMap ( wordMap )
    classLabelList = getClassLabelListFromDocumentDict ( documentDict )
    parameterDict = calculateParameter ( documentDict , totalWords , classLabelList )
    parameterFilename = getAbsolutePath ( textPath , "store/parameterDict.pickle" )
    storeParameterDict ( parameterFilename , parameterDict )
