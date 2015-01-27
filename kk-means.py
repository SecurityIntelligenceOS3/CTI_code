from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import numpy as np
from pymongo import MongoClient


#connect to mongoDB database
client = MongoClient('localhost', 27017)
db = client['test_database_py']
collection = db['test_collection']

data = collection.find()
dataCount = collection.count()

corpus = []

for document in data:
	paste = document['paste']
	str1 = ''.join(paste)
	corpus.append(str1)

cluster_numbers = 30
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(corpus)
#for i in range(len(vectorizer.get_feature_names())):
#print "WORD : ",vectorizer.get_feature_names()[25555]
model = KMeans(n_clusters=cluster_numbers, init='k-means++', max_iter=5000, n_init=1,verbose=1)
clusters = model.fit_predict(X)
print X.shape
print clusters.shape
for i in range(cluster_numbers):
	print "Cluster", i, " will contain association with the following documents: ",np.where(clusters == i)
#X_cluster_0 = X[cluster_0]
#print "X_CLUSTER_ 000",X_cluster_0
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(cluster_numbers):
    print "Cluster %d:" % i,
    for ind in order_centroids[i, :20]:
        print ' %s' % terms[ind],
    print
