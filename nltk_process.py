import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test_database_py']
collection = db['test_collection']

data = collection.find()

#define stopWords
stopWords = nltk.corpus.stopwords.words('english') + [
'.',
',',
'--',
'\'s',
'?',
')',
'(',
':',
'\'',
'\'re',
'"',
'-',
'}',
'{',
'%',
'[',
']',
'*',
'=',
'==',
';',
'+',
'>',
'<',
'$',
'//',
'''''',
'/',
'|',
'@'
]

for document in data:
	url = document['url']
	paste = document['paste']
	str1 = ''.join(paste)
	tokens = nltk.word_tokenize(str1.lower())
	for t in tokens:
		if t not in stopWords:
			print "Words: ",filter(lambda x: x not in stopwords.words('english'),t)


