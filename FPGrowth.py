import glob
import re
import nltk
from nltk import pos_tag, word_tokenize
import csv
import os
from fp_growth import find_frequent_itemsets

pattern = re.compile("[A-Za-z0-9]+")

re4='.*?'	
re5='(#)'	
re6='(#)'

rg2 = re.compile(re4+re5+re6,re.IGNORECASE|re.DOTALL)
fileList=glob.glob("/media/sherin/New Volume/DBMS PROJECT/A-Holistic-Lexicon-Based-Approach-to-Opinion-Mining-master/FP_Output/*.txt")
print "Extracting sentences..."
for filename in fileList:
	head, tail = os.path.split(filename)
	base=os.path.splitext(tail)[0]
	print base
	inFile = open(filename, 'r').read().split('\n')
	outFile=open(head+"/Processed Files/"+base+".txt",'w')
	for lines in inFile:
		
		modifiedLine = re.sub(rg2," ", lines)
		outFile.write('\n'+modifiedLine)
	outFile.close()
print "POS tagging..."
print "Extracting features..."
modifiedFileList=glob.glob("/media/sherin/New Volume/DBMS PROJECT/A-Holistic-Lexicon-Based-Approach-to-Opinion-Mining-master/FP_Output/Processed Files/*.txt")
for filename in modifiedFileList:
	sentenceNounList=[]
	head2, tail2 = os.path.split(filename)
	base=os.path.splitext(tail2)[0]
	posFile=open(head+"/POS tagged/"+base+".txt",'w')
	for line in open(filename,'r').readlines():
		tokens = word_tokenize(line)
		tags=pos_tag(tokens)
		nouns=[]
		for t in tags:
			m = re.match(pattern,t[0])
     			if m:
				if len(t[0])>2:
					posFile.write('\n'+str(t))	
					if t[1][0] == 'N':
						nouns.append(t[0])
                	
		sentenceNounList.append(nouns)
	posFile.close()
	with open(head+"/CSV/"+base+".csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(sentenceNounList)
	f.close()

	npFile=open(head+"/NounPhrases/"+base+".txt",'w')
	sentencePhrases=[]
	for itemset in find_frequent_itemsets(sentenceNounList,5):
		npFile.write('\n'+str(itemset))
		sentencePhrases.append(itemset)
	npFile.close()
	for phrases in sentencePhrases:
		if len(phrases)==2:
			inFile=open(head+"/Processed Files/"+base+".txt",'r')
			for line in inFile:
			
				
	






