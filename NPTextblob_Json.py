from nltk import word_tokenize
from textblob import TextBlob
import nltk
import glob
import json

#List to store the list generated from each noun phrase file of the data set 
GlobalNPList=[]

#Getting all the dataset files from given directory
fileList=glob.glob("C:/Users/Vinod Chhapariya/Desktop/TDBMS/Benchmark Dataset/*.txt")

#printing file names
for filename in fileList:
        print filename

#Noun Phrase Extraction for each file starts
for filename in fileList:

        #list to store noun phrases 
        NPList=[] 

        #Creating or overwritting noun phrase text file
        fileNounPhraseWrite=open(filename+"_NP",'w') 

        #tokenization for each line of given dataset file and using textblob method to generate noun phrases of tokenized line
        for line in open(filename,'r').readlines():
                tokens = word_tokenize(line)
                tb=TextBlob(line)
                nounPhrases=tb.noun_phrases

                #copying noun phrases to jsonList and writing each noun phrase to file
                for np in nounPhrases:
                        NPList.append(np)
                        fileNounPhraseWrite=open(filename+"_NP",'a')  
                        fileNounPhraseWrite.write('\n'+ str(np))

        fileNounPhraseWrite.close()

        #creating/ooverwriting json noun phrase file 
        with open(filename+'_NP.json', 'w') as fp:
                json.dump(NPList, fp)

        #adding NP List from each file to global NP list       
        GlobalNPList.append(NPList)
        print NPList
        print len(NPList)
        
print GlobalNPList
