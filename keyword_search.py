from pymongo import MongoClient
import re
import pymongo
#connect to mongoDB database
client = MongoClient('localhost', 27017)
db = client['test_database_py']
collection = db['test_collection']
#remove duplicates
collection.ensure_index( [("paste",pymongo.ASCENDING), ("unique",True), ("dropDups",True )] )
#remove empty pastes
collection.remove({"paste":[]})

#define your keywords
keyword = ['mail','hack']


for i in range(len(keyword)):
        print "KEYWORDS : ",keyword[i]
        query = {"paste":{'$regex':'.*'+keyword[i]+'.*'}}
        cursor = collection.find(query)
	print "There are : ",cursor.count()," results that match search for \" ", keyword[i],"\""
	for key in cursor:

		url = key['url']
		paste = key['paste']
		print"--------------------------URL-------------------------"
		print url
		print"-----------------PASTE--------------------------------"
		print paste

		for j in paste:
		        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<"
		        count = 0
		        key = []
		        for word in j.split():
		                for kk in range(len(keyword)):
		                        combination =".*"+ keyword[kk]+".*"
		                        searchWord = re.search(combination, word)
		                        if searchWord is not None:
		                               # print "It FOUND :", keyword[i]
		                                count=count+1
		                        else:
		                                pass
		        print "----------------Keyword : ",keyword[i],"  appeared ",count," times --------------\n\n"






	    #print key

