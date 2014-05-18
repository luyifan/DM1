import sys
import os
import pickle
import math
from getWordDict import getAbsolutePath
from calculateParameterDict import  loadWordMap
from preprocessingDocumentDict import getOneDocumentList
reload ( sys )
sys.setdefaultencoding ( 'utf-8' )

def loadParameterDict ( filename ):
    with open ( filename , "rb" ) as parameterPickleFile:
        parameterDict = pickle.load ( parameterPickleFile )
        parameterPickleFile.close ()
    return parameterDict

def predictDocument ( filename , wordMap , parameterDict ):
    wordList = getOneDocumentList ( filename , wordMap )
    maxClassLabel = -1
    maxAns = -1E30
    for classLabel in parameterDict [ "prior" ]:
        ans = math.log ( parameterDict [ "prior" ][ classLabel ] )
        for wordId in wordList:
            ans += math.log ( parameterDict [ "maxwordlikelihood" ][ classLabel ][ wordId ] )
        if ans > maxAns:
            maxAns = ans
            maxClassLabel = classLabel
    return maxClassLabel

def predictDocumentInDir ( predictPath , wordMap , parameterDict ):
    answerDict ={};
    predictList = os.listdir ( predictPath )
    for predictFile in predictList:
        filename  = getAbsolutePath ( predictPath , predictFile )
        predictDocumentId =int( predictFile.split(".") [ 0 ] ) ;
        classLabel = predictDocument ( filename , wordMap , parameterDict )
        answerDict [ predictDocumentId ] = classLabel
    return answerDict

def storeAnswer ( filename , answerDict ):
    answerFile = open( filename , "w" )
    answerFile.write ( "Id,Category\n" )
    sortedDocument = sorted ( answerDict.items() , key = lambda x:x[0] , reverse = False )
    for item in sortedDocument:
        answerFile.write (str( item[ 0 ] ))
        answerFile.write ( "," )
        answerFile.write (str( item[ 1 ] ))
        answerFile.write ( "\n" )
    answerFile.close ()
if __name__ == "__main__":
    textPath = sys.argv [ 1 ];
    predictPath = getAbsolutePath ( textPath , "test" )
    wordMapFilename = getAbsolutePath ( textPath , "store/wordDictByThreshold.pickle"  )
    wordMap = loadWordMap ( wordMapFilename )
    parameterFilename = getAbsolutePath ( textPath , "store/parameterDict.pickle" )
    parameterDict = loadParameterDict ( parameterFilename )
    answerDict = predictDocumentInDir ( predictPath , wordMap , parameterDict )
    answerFilename = getAbsolutePath ( textPath , "textAnswer.csv" )
    storeAnswer ( answerFilename , answerDict )
