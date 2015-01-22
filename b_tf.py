from math import log
from pymongo import MongoClient


# XXX: Enter in a query term from the corpus variable
QUERY_TERMS = ['attack','hack']
def tf(term, doc, normalize=True):
        doc = doc.lower().split()
        if normalize:
                try:
                        return float(doc.count(term.lower())) / float(len(doc))
                except ZeroDivisionError:
                        return 0.0
        else:
                return doc.count(term.lower()) / 1.0

def idf(term, corpus):
        num_texts_with_term = len([True for text in corpus if term.lower()
        in text.lower().split()])
        try:
                return 1.0 + log(float(len(corpus)) / num_texts_with_term)
        except ZeroDivisionError:
                return 1.0

def tf_idf(term, doc, corpus):
        return tf(term, doc) * idf(term, corpus)
#connect to mongoDB database
client = MongoClient('localhost', 27017)
db = client['test_database_py']
collection = db['test_collection']

data = collection.find()
dataCount = collection.count()

corpus = {}
query_scores = {}
for document in data:
	objectID = document['_id']
	paste = document['paste']
	str1 = ''.join(paste)
	corpus [objectID] = str1
	# Score queries by calculating cumulative tf_idf score for each term in query
	query_scores [objectID] = 0
#Lower 
for term in QUERY_TERMS:
	for doc in corpus:
		tfResult=tf(term, corpus[doc])
		if tfResult != 0.0:
			print "TF Doc:",doc,tfResult,"->",term
	idfResult=idf(term, corpus.values())
	if idfResult != 0.0:
		print "IDF: ",term,"->",idfResult
	for doc in corpus:
		score = tf_idf(term, corpus[doc], corpus.values())
		if score != 0.0:
			print "TF_IDF: ", doc,term,"->", score
		query_scores[doc] += score	
		
	print "Overall TF-IDF scores for query '%s'" % (' '.join(QUERY_TERMS), )
	for (doc, score) in sorted(query_scores.items()):
                if score != 0.0:
                        print doc, score

