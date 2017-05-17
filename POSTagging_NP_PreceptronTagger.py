from nltk.tag import PerceptronTagger
from nltk.data import find
import glob


#code for loading perceptron tagger 
PICKLE = "averaged_perceptron_tagger.pickle"
AP_MODEL_LOC = 'file:'+str(find('taggers/averaged_perceptron_tagger/'+PICKLE))
tagger = PerceptronTagger(load=False)
tagger.load(AP_MODEL_LOC)
pos_tag = tagger.tag


#list to store POS and NP lists generated from each file
GlobalPOSList=[]
GlobalNPList=[]

#getting filenames of dataset files
fileList=glob.glob("C:/Users/Vinod Chhapariya/Desktop/TDBMS/Benchmark Dataset/*.txt")

#printing filenames
for filename in fileList:
        print filename

#POS tagging using Preceptron tagger        
for filename in fileList:
        POSList=[]
        NPList=[]
        filePOSTagWrite=open(filename+"_POSTag_Perceptron",'w')
        for line in open(filename,'r').readlines():
                tags=pos_tag(line.split())

                for t in tags:
                        POSList.append(t)
                        filePOSTagWrite=open(filename+"_POSTag_Perceptron",'a')
                        filePOSTagWrite.write('\n'+str(t))
                #for each pos tag if penn tree symbol starts from N then add to NPList
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
