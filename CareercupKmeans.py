# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:21:11 2016
@author: lalit
"""

####################################################################################
#Once the LDA devides the document in topics.We use Kmeans on every topics to
#devide further in clusters. Veryfy clusters visibly to determine clustering accuracy.
####################################################################################

import pandas as pd,os,math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

G1=G2=G3=G4=G5=0 #Level variables for Final plots
#Open cleaned file written in LDA code and splt on dot delimiter.
filerw=open('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\clean_file.txt').read()#.split(".")#.split(" . ")
doc=[x for x in filerw.split('.') if x]
columns = ['question','topic'] #define dataframe columns
df = pd.DataFrame(columns=columns) 
topic=open('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\topic_mixture_per_doc.txt').read().split("\n")

#Create the dataframe with questions and topic numbers
for count,d in enumerate(doc):
    df=df.append({'question': d,'topic':topic[count]}, ignore_index=True)
df.index = np.arange(1, len(df)+1) #Rearrange df index from 1 instead of 0(default)          

#Group df by topic numbers and read groups and add it to topic_clusters list.
LDA_topics = df['question'].groupby(df['topic'])

for g in range(0,1):  #Repeat For each topic,Hardcoded LDA topic count
    topic_clusters=[]
    #Get groups from 0 to n and fetch its questions
    questions=list(LDA_topics.get_group(str(g))) 
    #print ("\n"+"Topic : "+str(g))
    for count,q in enumerate(questions):
     #   print ("Question "+str(count+1)+" :"+str(q)) #Print questions in each topic
        topic_clusters.insert(count,q) # Create topic clusters from get group questions 
    
    true_k = 4
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, strip_accents="unicode", use_idf=True, norm="l2")
    X = vectorizer.fit_transform(topic_clusters) #fit new topic_clusters in each loop for every topic/group
    KMN = KMeans(n_clusters=true_k, max_iter=100, n_init=1) 
    KMN.fit(X)
    #print("Top terms in Topic:"+g)
    order_centroids = KMN.cluster_centers_.argsort()[:, ::2]
    terms = vectorizer.get_feature_names()
    #print ("Top Terms in "+str(true_k)+" clusters :")    
    #for i in range(true_k):
     #   print ""
      #  print "Cluster %d:" %(i),
       # for ind in order_centroids[i, :2]: # number of words in cluster 
        #    print ' %s' % terms[ind],
    clusters = KMN.labels_.tolist()
    print ("\n"+str(clusters)+"\n") #Print the cluster labels for each question
    
    #Compare cluster questions to each other and decide similarity levels 1-5     
    Resultfile1="C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\Result.txt"
    
    loopval=WG5=0   
    xlbl = ('Incorrect Clusters','correct Clusters') 
    y_pos = np.arange(len(xlbl))

    if(os.path.exists(Resultfile1)==True):
        #print("Evaluation file exists, Do you want to use evaluatin results ? Y or No Q to quit")
        user_input = raw_input('A evaluation file already exits! Do you want to use previous results Y or N ? ')
        if user_input == 'Y':
            FRES=open(Resultfile1).read().split("\n")#line()#.split(".")#.split(" . ")
        
            for m in clusters:
                for n in clusters:
                    if (int(FRES[loopval])==5 and clusters[m]==clusters[n]):
                        G5=G5+1
                    elif (int(FRES[loopval])==1 and clusters[m]==clusters[n]):
                        WG5+=1
                    elif (int(FRES[loopval])==5 and clusters[m]!=clusters[n]):
                        WG5+=1
                    elif (int(FRES[loopval])==1 and clusters[m]!=clusters[n]):
                        G1=G1+1
                    loopval+=1
            print("Clustering algorithm accuracy :" + str((float(G5+G1)/float(len(FRES)))*100))
            questCount = [WG5,(G1+G5)] 
            plt.bar(y_pos, questCount, align='center', alpha=0.6)
            
            plt.grid(zorder=0)
            plt.xlabel('Questions similarity levels')
            plt.ylabel('Number of comparisions')
            plt.title('KMeans clustering accuracy chart')
            plt.xticks(y_pos, xlbl)
            plt.legend()
            plt.tight_layout()
            plt.show()
            
        elif user_input == 'N':
            for counta,a in enumerate(topic_clusters):
                for countb,b in enumerate(topic_clusters):
                    print ("how are below 2 questions are similar ?"+"\n")                
                    print ("Q"+str(counta+1)+" : "+topic_clusters[counta])
                    print ("Q"+str(countb+1)+" : "+topic_clusters[countb])
                    #print("Q"+str(counta+1)+" cluster :"+str(clusters[counta])+" Q"+str(countb+1)+" cluster :"+str(clusters[countb]))
                    choice = [1,5]                    
                    while True: #Validate use input to be int and equals to 1 or 5
                        try:
                            num = int(raw_input("Please enter a match level from 1 to 5 :"))
                            if num in choice:
                                #print("inside if")    
                                #type(1)
                                break
                        except ValueError:
                            print "Oops! That was not a valid number.  Try again!"
                    #Increase the Level counts for each of the user's decision.
                    if (num==5 and clusters[counta]==clusters[countb]):
                        G5=G5+1
                    elif (num==1 and clusters[counta]==clusters[countb]):
                        WG5+=1
                    elif (num==5 and clusters[counta]!=clusters[countb]):
                        WG5+=1
                    elif (num==1 and clusters[counta]!=clusters[countb]):
                        G1=G1+1
                    print ("")
    
            print("You have reviewed 50 questions.")
            print("Clustering algorithm accuracy :" + str(((float(G5+G1)/float(64))*100)))
            questCount = [WG5,(G1+G5)] 
            plt.bar(y_pos, questCount, align='center', alpha=0.6)
            
            plt.grid(zorder=0)
            plt.xlabel('Questions similarity levels')
            plt.ylabel('Number of comparisions')
            plt.title('KMeans clustering accuracy chart')
            plt.xticks(y_pos, xlbl)
            plt.legend()
            plt.tight_layout()
            plt.show()
            
        elif user_input == 'q':break
    

print("---- Legends ----")
print("Incorrect Clusters : Has most similar questions falling into different clusters or vice-versa")
print("Correct Clusters : Has most similar questions falling into same clusters or vice-versa")
print("-----------------")

#Set the LABELs,Titles and plot the Bar chart.

