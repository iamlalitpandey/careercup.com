# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:21:11 2016
@author: lalit
"""

####################################################################################
#Once the LDA devides the document in topics.We use Kmeans on every topics to
#devide further in clusters. Veryfy clusters visibly to determine clustering accuracy.
####################################################################################

import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

filerw=open('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\clean_file.txt').read()#.split(".")#.split(" . ")
doc=[x for x in filerw.split('.') if x]
columns = ['question','topic'] #define dataframe columns
df = pd.DataFrame(columns=columns) 
topic=open('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\topic_mixture_per_doc.txt').read().split("\n")
frw=open('Rff.txt','a+')
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
    frw.write("\n"+"Topic : "+str(g)+"\n")
    for count,q in enumerate(questions):
        frw.write("\n"+"Question "+str(count+1)+" :"+str(q)+"\n") #Print questions in each topic
        topic_clusters.insert(count,q) # Create topic clusters from get group questions 
    
    true_k = 2
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, strip_accents="unicode", use_idf=True, norm="l2", min_df = 2,max_df = 5)
    X = vectorizer.fit_transform(topic_clusters) #fit new topic_clusters in each loop for every topic/group
    KMN = KMeans(n_clusters=true_k, max_iter=100, n_init=1) 
    KMN.fit(X)
    #print("Top terms in Topic:"+g)
    order_centroids = KMN.cluster_centers_.argsort()[:, ::2]
    terms = vectorizer.get_feature_names()
    #print ("Top Terms in "+str(true_k)+" clusters :")    
    #for i in range(true_k):
        #print ""
        #print "Cluster %d:" %(i),
       # for ind in order_centroids[i, :2]: # number of words in cluster 
        #    print ' %s' % terms[ind],
    clusters = KMN.labels_.tolist()
    #print ("\n"+str(clusters)+"\n") #Print the cluster labels for each question
    
    