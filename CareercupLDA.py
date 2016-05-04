"""
Using Latent Dirichlet Allocation for topic modeling. 
"""
from sklearn.feature_extraction.text import CountVectorizer
import lda
#from nltk.corpus import stopwords
#stopwords=stopwords.words("english") 
import numpy as np
import re
topic_num=30

#tokenization
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
                                
#read the dataset                
data=open('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\dataset.txt').read()#split('EndOfQuestion')
doc0=re.sub('---.*?---',' ',data) 
doc1=re.sub('[^a-zA-Z]',' ',doc0)#replace chars that are not letters or numbers with a space
doc2=re.sub('EndOfQuestion','.',doc1)
doc3=re.sub(' +',' ',doc2)#remove duplicate spaces
doc4=re.sub(' \.','.',doc3)
doc5=re.sub('\. ','.',doc4.lower())
docs=[x for x in doc5.split('.') if x]
#len(docs)

filew=open('clean_file.txt','a+')
for i in docs:
    filew.write(i+'.')        
filew.close()

matrix = tf_vectorizer.fit_transform(doc3.split(" . "))
#print matrix

#get the vocabulary
vocab=tf_vectorizer.get_feature_names()

#initialize the LDA model
model = lda.LDA(n_topics=topic_num, n_iter=500)

#fit the model to the dataset
model.fit(matrix)

#write the top terms for each topic
top_words_num=20
topic_mixes= model.topic_word_
#print len(topic_mixes)

fw=open('top_terms_per_topic.txt','w')
for i in range(topic_num):#for each topic
    sorted_indexes=np.argsort(topic_mixes[i])[len(topic_mixes[i])-top_words_num:]#get the indexes of the top-k terms in this topic
    sorted_indexes=sorted_indexes[::-1]#reverse to get the best first    
    my_top=''
    for ind in sorted_indexes:my_top+=vocab[ind]+' ' 
    fw.write('TOPIC: '+str(i)+' --> '+str(my_top)+'\n')
fw.close()

#write the top topics for each doc
top_topics_num=1
doc_mixes= model.doc_topic_
print len(doc_mixes)
fw=open('topic_mixture_per_doc.txt','w')
for i in range(len(doc_mixes)):#for each doc
    sorted_indexes=np.argsort(doc_mixes[i])[len(doc_mixes[i])-top_topics_num:]#get the indexes of the top-k topics in this doc
    sorted_indexes=sorted_indexes[::-1]#reverse to get the best first    
    my_top=''
    for ind in sorted_indexes:my_top+=''+str(ind)###############+'.'+str(int((round(doc_mixes[i][ind],2))*100))
    fw.write(str(my_top)+'\n')
    
fw.close()
