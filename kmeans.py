# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:21:11 2016
@author: lalit
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

G1=G2=G3=G4=G5=0
filerw=open('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\clean_file.txt').read()#.split(".")#.split(" . ")
doc=[x for x in filerw.split('.') if x]
columns = ['question','topic']
df = pd.DataFrame(columns=columns)
topic=open('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\topic_mixture_per_doc.txt').read().split("\n")
for count,d in enumerate(doc):
    df=df.append({'question': d,'topic':topic[count]}, ignore_index=True)
df.index = np.arange(1, len(df)+1)          

LDA_topics = df['question'].groupby(df['topic'])
for g in range(0,2):
    topic_clusters=[]
    questions=list(LDA_topics.get_group(str(g))) 
    
    print ("\n"+"Topic : "+str(g))
    for count,q in enumerate(questions):
        print ("Question "+str(count+1)+" :"+str(q))                  #Print questions in each topic
        topic_clusters.insert(count,q)
    
#    print topic_clusters
    true_k = 3
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, strip_accents="unicode", use_idf=True, norm="l2", min_df = 2,max_df = 5)
    X = vectorizer.fit_transform(topic_clusters)
    KMN = KMeans(n_clusters=true_k, max_iter=100, n_init=1)
    KMN.fit(X)
    #print("Top terms in Topic:"+g)
    order_centroids = KMN.cluster_centers_.argsort()[:, ::2]
    terms = vectorizer.get_feature_names()
    print ("Top Terms in "+str(true_k)+" clusters :")    
    for i in range(true_k):
        print ""
        print "Cluster %d:" %(i),
        for ind in order_centroids[i, :2]: # number of words in cluster 
            print ' %s' % terms[ind],
    clusters = KMN.labels_.tolist()
    print ("\n"+str(clusters)+"\n") 
        
    for counta,a in enumerate(topic_clusters):
        for countb,b in enumerate(topic_clusters):
            print ("how are below 2 questions are similar ?"+"\n")                
            print ("Q"+str(counta+1)+" : "+topic_clusters[counta])
            print ("Q"+str(countb+1)+" : "+topic_clusters[countb])
            print("Q"+str(counta+1)+" cluster :"+str(clusters[counta])+" Q"+str(countb+1)+" cluster :"+str(clusters[countb]))
            
            while True:
                try:
                    num = int(raw_input("Please enter a match level from 1 to 5 :"))
                    if (num<6 and num>0):break
                except ValueError:
                    print "Oops! That was not a valid number.  Try again!"
            
            if (num==1):G1=G1+1
            elif(num==2):G2+=1
            elif(num==3):G3+=1
            elif(num==4):G4=G4+1
            elif(num==5):G5=G5+1
            print ("")

questCount = [G1,G2,G3,G4,G5]
accuracyPct=float(questCount[3]+questCount[4])/float(sum(questCount))*100
print("You have reviewed " +str(sum(questCount))+" questions.")            
print("According to your ratings Clustering accuracy is :"+str(accuracyPct)+"%")

print("----------------------------- Legends ----------------------------")
print("Level 1 : 00% similar same cluster or 100% similar different cluster")
print("Level 2 : 25% similar same cluster or 75% similar different cluster")
print("Level 3 : 50% similar same cluster or 50% similar different cluster")
print("Level 4 : 75% similar same cluster or 25% similar different cluster")
print("Level 5 : 75% similar same cluster or 00% similar different cluster")
print("------------------------------------------------------------------")





xlbl = ('Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5')
y_pos = np.arange(len(xlbl))

plt.bar(y_pos, questCount, align='center', alpha=0.5)
plt.xlabel('Questions similarity levels')
plt.ylabel('Number of questions')
plt.title('KMeans clustering accuracy chart')
plt.xticks(y_pos, xlbl)
plt.legend()
plt.tight_layout()
plt.show()
