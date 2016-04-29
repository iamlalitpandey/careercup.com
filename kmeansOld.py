"""
A simple script that demonstrates how we classify textual data with sklearn.
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans

#read the reviews and their polarities from a given file
def loadData(fname):
    questions=[]
    #labels=[]
    f=open(fname)
    for line in f:
        question=line.split('EndofQuestion')
        questions.append(question)    
        #labels.append(int(rating))
    
    f.close()
    return questions#,labels

#rev_train,labels_train=loadData('reviews_train.txt')
#rev_test,labels_test=loadData('reviews_test.txt')
questions=loadData('dataset.txt')
#print questions[3]
#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(questions)

#count the number of times each term appears in a document and transform each doc into a count vector
#counts_train = counter.transform(rev_train)#transform the training data
transQuestions= counter.transform(questions)#transform the testing data

#build a 3-NN classifier on the training data
#data=[88888888888888880000],[0],[1],[10101],[010101],[3453522],[01010101],[11111],[01110000],[45343]

KMEANS = KMeans()
predicted=KMEANS.fit_predict(questions)

#KNN=KNeighborsClassifier(5) 
#KNN.fit(counts_train,labels_train)

#use the classifier to predict

centroids = KMEANS.cluster_centers_
print centroids
print predicted

print KMEANS.score


for i in (0,len(labels_test)):
    print len(predicted)
    print len(labels_test)

#print predicted
#print the accuracy
print accuracy_score(predicted,labels_test)
print accuracy_score(predicted,labels_train)