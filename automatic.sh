#!bin/sh
python getWordDict.py /Users/maxluyifan/Desktop/data
python preprocessingWordDict.py /Users/maxluyifan/Desktop/data 0.4
python preprocessingDocumentDict.py /Users/maxluyifan/Desktop/data
python calculateParameterDict.py /Users/maxluyifan/Desktop/data
python predictDocumentClassLabel.py /Users/maxluyifan/Desktop/data
