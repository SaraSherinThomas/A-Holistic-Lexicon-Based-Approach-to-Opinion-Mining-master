from nltk import pos_tag, word_tokenize
from textblob import TextBlob
import nltk
import glob

#list for POS and NP
GlobalPOSList=[]
GlobalNPList=[]

#getting list of dataset files
fileList=glob.glob("C:/Users/Vinod Chhapariya/Desktop/TDBMS/Benchmark Dataset/*.txt")

#printing file names
for filename in fileList:
        print filename

#pos tagging and noun phrase extraction for each file 
for filename in fileList:
        filePOSTagWrite=open(filename+"_POSTag",'w')

        #lists for POS tags and noun phrases 
        POSList=[]
        NPPList=[]
        for line in open(filename,'r').readlines():
                tokens = word_tokenize(line)
                tb=TextBlob(line)
                        
                #POS Tagging using NLTK Tagger
                tags=pos_tag(tokens)
                for t in tags:
                        POSList.append(t)
                        filePOSTagWrite=open(filename + "_POSTag",'a')
                        filePOSTagWrite.write('\n'+str(t))
                #for each tag check whether its penn tree symbol starts with N, if yes add that tag to noun phrase list 
                for t in tags:
                        if t[1][0] == 'N':
                                NPList.append(t[0])
        filePOSTagWrite.close()

        #adding POS and NP list for each file to global list(list in a list)
        GlobalPOSList.append(POSList)
        GlobalNPList.append(NPList)

        #printing length of each list
        print len(POSList)
        print len(NPList)

print len(GlobalPOSList)
print len(GlobalNPList)
