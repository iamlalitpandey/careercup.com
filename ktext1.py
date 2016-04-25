# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:21:11 2016

@author: lalit
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
#from sklearn.metrics import adjusted_rand_score

filerw=open('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\file.txt').read()#.split(".")#.split(" . ")
doc=[x for x in filerw.split('.') if x]

len(doc)


#print doc[0][2]
columns = ['question','topic']
#indexx=index=range(1,1120)
df = pd.DataFrame(columns=columns)
#len(doc)
topic=open('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\topic_mixture_per_doc.txt').read().split("\n")
for count,d in enumerate(doc):
    df=df.append({'question': d,'topic':topic[count]}, ignore_index=True)
df.index = np.arange(1, len(df)+1)          
#len(df)                                            
#df.loc[2]

 # questions in groups
#df
#for name, group in df.groupby('topic'): 
#    print name,group

#groupedDF=df.groupby(df['topic'])
#print groupedDF.get_group('0')

LDA_topics = df['question'].groupby(df['topic'])
for g in range(0,10):
    topic_clusters=[]
    questions=list(LDA_topics.get_group(str(g))) 
    
    print ("\n"+"Topic : "+str(g))
    for count,q in enumerate(questions):
       # print q                  #Print questions in each topic
        topic_clusters.insert(count,q)
    
#    print topic_clusters
    true_k = 3
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(topic_clusters)
    KMN = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    KMN.fit(X)
    #print("Top terms in Topic:"+g)
    order_centroids = KMN.cluster_centers_.argsort()[:, ::2]
    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        print ""       
        print "Cluster %d:" % i,
        for ind in order_centroids[i, :3]: # number of words in cluster 
            print ' %s' % terms[ind],
            

    clusters = KMN.labels_.tolist()
    print ("\n"+str(clusters)+"\n") 
    

#for t in LDA_topics:
#    print type(t)


#LDA_topics = df.groupby('topic')
#for t in LDA_topics:
    
    
#for row in df.itertuples():
#     if row[2]==2:
#         print(row)
         ########################### Ignore below KMeans sample Code ##############
documents = ["we are preparing for Amazon interview in chennai and looking friends to join for group study pls share your contact sivarasu net gmail com if u r interested Amazon SDE",
"There was a bug caught in production why it wasn t caught in the qa what was the reason Amazon Quality Assurance Engineer Testing",
"youtube video audio is audible and rest all r working fine doesn t show up only in firefox browser how would you debug this issue Amazon Quality Assurance Engineer",
"Implement a test Automation framework for the gmail login page Amazon Quality Assurance Engineer Automata",
"Write down testcases for an app which uploads files text or pdf etc from local machine or a dropbox Also cover testcases for the narration of that file Amazon Quality Assurance Engineer Testing",
"Find the minimum index distance sum of words For example arr input The result should be since the nd and s distance are and abs abs abs Implement this in O N Amazon SDE Algorithm "]

true_k = 3
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)
KMN = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
KMN.fit(X)
print("Top terms per cluster:")
order_centroids = KMN.cluster_centers_.argsort()[:, ::1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print "Cluster %d:" % i,
    for ind in order_centroids[i, :1]: # number of words in cluster 
        print ' %s' % terms[ind],
    print

clusters = KMN.labels_.tolist()
print clusters

