from pymongo import MongoClient
#include pprint for readabillity of the 
from pprint import pprint

#change the MongoClient connection string to your MongoDB database instance
c = MongoClient()
db=c.trial

ASingleReview = db.reviews.find_one({})
print('A sample document:')
pprint(ASingleReview)

result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 1}})
print('Number of documents modified : ' + str(result.modified_count))

UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)

"""If you wanted to update all the fields of the document and keep the same 
ObjectID you will want to use the replace_one function."""