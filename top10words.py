import sys
import os
import pickle
from getWordDict import getAbsolutePath
from calculateParameterDict import loadWordMap
from predictDocumentClassLabel import loadParameterDict
reload ( sys )
sys.setdefaultencoding ( 'utf-8' )

def calculateTopK ( parameterDict , topK ):
    relativeProbability = {};
    topKDict ={};
    for classLabel in parameterDict [ "prior" ]:
        relativeProbability [ classLabel ] = {}
        for wordId in parameterDict [ "maxwordlikelihood" ][ classLabel ]:
            temp = 0 ;
            for notclassLabel in parameterDict [ "prior" ]:
                if notclassLabel != classLabel:
                    if wordId in parameterDict [ "maxwordlikelihood" ][ notclassLabel ]:
                        temp += parameterDict [ "maxwordlikelihood" ][ notclassLabel ][ wordId ]
            temp = parameterDict [ "maxwordlikelihood" ][ classLabel ][ wordId ]/temp
            relativeProbability [ classLabel ][ wordId ] = temp
        sortedWords = sorted ( relativeProbability [ classLabel ].items() , key = lambda x:x[ 1 ] , reverse = True )
        topKDict [ classLabel ] = []
        k = 0
        for item in sortedWords:
            k += 1
            topKDict[ classLabel ].append ( item )
            if topK == k:
                break
    return topKDict
def storeTopK ( filename , topKDict , wordIdMap ):
    f = open ( filename , "w" )
    for classLabel in topKDict:
        f.write ( "ClassLabel" + str ( classLabel ) )
        f.write ( "\n" )
        for item in topKDict [ classLabel ]:
            f.write ( wordIdMap [ item [ 0 ] ] + " " + str ( item[ 1 ] ) + "\n" )
    f.close()
if __name__ == "__main__":
    textPath = sys.argv[ 1 ]
    topK =int ( sys.argv [ 2 ] )
    wordMapFilename = getAbsolutePath ( textPath , "store/wordDictByThreshold.pickle"  )
    wordMap = loadWordMap ( wordMapFilename )
    parameterFilename = getAbsolutePath ( textPath , "store/parameterDict.pickle" )
    parameterDict = loadParameterDict ( parameterFilename )
    topKDict = calculateTopK ( parameterDict , topK )
    #print ( topKDict )
    wordIdMap = {} ;
    for word in wordMap:
        wordIdMap [ wordMap [ word ] ] = word
    topKFilename = getAbsolutePath ( textPath , "topK.txt" )
    storeTopK ( topKFilename ,  topKDict , wordIdMap )

