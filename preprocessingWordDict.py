import pickle
import sys
import os
from getWordDict import getAbsolutePath
reload ( sys )
sys.setdefaultencoding ( 'utf-8' )

def getWordDictByThreshold ( oldWordDict , highPrecision ):
    totalDocuments = oldWordDict[ "totalDocuments" ];
    newWordDict = {};
    newWordDictFrequency ={}
    wordId = -1
    #print ( highPrecision )
    #print ( totalDocuments )
    #print ( highPrecision * totalDocuments )
    highFrequency = int ( highPrecision * totalDocuments );
    for word in oldWordDict [ "words" ]:
        timesInDocuments = oldWordDict [ "words" ][ word ] ;
        if timesInDocuments < highFrequency:
            wordId += 1
            newWordDictFrequency [ word ] = timesInDocuments
            newWordDict [ word ] = wordId
    return ( newWordDict , newWordDictFrequency )

def getWordDictFromPickle ( wordPickleFilename ):
    with open ( wordPickleFilename , "rb" ) as wordPickleFile:
        oldWordDict = pickle.load ( wordPickleFile )
        wordPickleFile.close ( )
    return oldWordDict
if __name__ == "__main__":
    textPath = sys.argv [ 1 ]
    wordPickleFilename = getAbsolutePath ( textPath , "store/wordDict.pickle" )
    highPrecision = float(sys.argv [ 2 ])
    oldWordDict = getWordDictFromPickle ( wordPickleFilename )
    (newWordDict , newWordDictFrequency ) = getWordDictByThreshold ( oldWordDict , highPrecision )
    #print newWordDict
    newWordPickleFilename = getAbsolutePath ( textPath , "store/wordDictByThreshold.pickle" )
    with open ( newWordPickleFilename , "wb"  ) as picklefile:
        pickle.dump ( newWordDict , picklefile )
        picklefile.close ( )
'''
    sorted_frequency = sorted ( newWordDictFrequency , key = newWordDictFrequency.get , reverse = True )
    ftest =  open ( "/Users/maxluyifan/Desktop/test.txt" , "w")
    for word in sorted_frequency:
        ftest.write ( word )
        ftest.write ( "\n" )
'''

