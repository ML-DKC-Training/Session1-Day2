from pymongo import MongoClient
# Connect to the MongoDB
client = MongoClient()
# Set the db object to point to the trial database
db=client.trial
# Showcasing the count() method of find, count the total number of 5 ratings 
print('The number of 5 star reviews:')
fivestarcount = db.reviews.find({'rating': 5}).count()
print(fivestarcount)
# now say we want to get all five star ratings grouped by cuisine
stargroup=db.reviews.aggregate(
# The Aggregation Pipeline is defined as an array of different operations
[
# The first stage in this pipe is to group data
{ '$group':
    { '_id': '$cuisine',
    "avg_rating": { "$avg": "$rating" },
  } 
},

    {"$sort" : 
                 { 'avg_rating' :1 }
    }
])
# Print the result
for group in stargroup:
    print(group)

"""
   {"rating":"$rating",
    "cuisine":'$cuisine'},

     "count" : 
                 { '$sum' :1 }
    }
},
"""
   
    

 