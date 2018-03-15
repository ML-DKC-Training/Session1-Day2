""" An example of how to connect to MongoDB """ 
import sys
from pymongo import MongoClient
from random import randint
from pymongo.errors import ConnectionFailure

# step 1: Connect to MongoDb server
try:
	c = MongoClient(host="localhost", port=27017) 
	print ("Connected successfully")
except ConnectionFailure:
	sys.stderr.write("Could not connect to MongoDB")
db = c.trial
# step 2: create sample data

names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

for x in range(1, 501):
    trial = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))]
        }
#Step 3: Insert trial object directly into MongoDB via isnert_one
    result=db.reviews.insert_one(trial) # insert_one will insert one document into MongoDb
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 100 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating 100 business reviews')