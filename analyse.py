from pymongo import MongoClient
import nltk
import re
from nltk import word_tokenize

#connect to mongoDB database
client = MongoClient('localhost', 27017)
db = client['test_database_py']
collection = db['test_collection']

#get all elements from database to analyse

data=collection.find()

#define pattern that will match the search

#pattern=r'(?x)([A-Z]\.)+|\$?\d+(\.\d+)?%?|\w+([-']\w+)*|[+/\-@&*]''

#Define English stop words

stop_words = nltk.corpus.stopwords.words('english') + [
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
]


for document in data:
        #Read the fields needed to furhter process in analyse
        url = document['url']
        paste = document['paste']
        uniq_visitors = document['uniq_visitors']
        # Time is stored in following format "Friday 16th of January 2015 07:51:58 AM CDT"
        time = document['time']
        #       print"--------------------------URL-------------------------"
#        print url
#        print"-----------------PASTE--------------------------------"
#        print paste
        for j in paste:
               # tokens = nltk.word_tokenize(j)
                #text=nltk.Text(tokens)

                #Counting how many types the keyword appeared in text

		count = 0
		variable = 0
		for word in j.split():
			searchWord=re.search(r"hack.*", word);
			if searchWord is not None:
				count=count+1
				variable=1
			#Split paste text in sentences

		       
		else:
			pass
        if variable == 1:
		txt = j
        	sentences = nltk.tokenize.sent_tokenize(txt)
		#tokens = [nltk.tokenize.word_tokenize(s) for s in sentences]
		#print tokens
		words = [w.lower() for sentence in sentences for w in
				nltk.tokenize.word_tokenize(sentence)]
		fdist = nltk.FreqDist(words)
		# Basic stats
		num_words = sum([i[1] for i in fdist.items()])
		num_unique_words = len(fdist.keys())
		# Hapaxes are words that appear only once
		num_hapaxes = len(fdist.hapaxes())
		top_10_words_sans_stop_words = [w for w in fdist.items() if w[0]
		not in stop_words][:10]
		
		print "----------------------------------------------------"
		print url,"\n"
		print "----------------------------------------------------"
		print j
		print "--------------------Analyze-------------------------"
		print "Searched word appeared : ",count," times"
		print "This post has ",uniq_visitors[0], "unique visitors "
		print "It was posted on : ", time[0]
		print "===================NLTK=============================" 
		print '\tNum Sentences:'.ljust(25), len(sentences)
		print '\tNum Words:'.ljust(25), num_words
		print '\tNum Unique Words:'.ljust(25), num_unique_words
		print '\tNum Hapaxes:'.ljust(25), num_hapaxes
		print '\tTop 10 Most Frequent Words (sans stop words):\n\t\t', \
		      '\n\t\t'.join(['%s (%s)'
		         % (w[0], w[1]) for w in top_10_words_sans_stop_words])	               # print "THis is the text",text
                #if text.concordance("hacking") is not "No matches" or text.concordance($
            #    for word in ["hacking"]:
            #            print text.concordance(word)


