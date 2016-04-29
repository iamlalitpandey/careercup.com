# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:21:11 2016

@author: lalit
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.stop_words STOP_WORDS
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
        print ("Question "+str(count)+" :"+str(q))                  #Print questions in each topic
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
    for i in range(true_k):
        print ""       
        print "Cluster %d:" % i,
        for ind in order_centroids[i, :5]: # number of words in cluster 
            print ' %s' % terms[ind],
            

    clusters = KMN.labels_.tolist()
    print ("\n"+str(clusters)+"\n") 
    
    
print df


#for t in LDA_topics:
#    print type(t)


#LDA_topics = df.groupby('topic')
#for t in LDA_topics:
    
    
#for row in df.itertuples():
#     if row[2]==2:
#         print(row)
         ########################### Ignore below KMeans sample Code ##############
