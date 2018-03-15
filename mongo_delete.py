
year_lst=[1980, 1988, 1990, 1992, 1993, 1998, 2002]

Leap_Years=list(filter(lambda leap_yrs:(leap_yrs%4==0),year_lst))

print("Leap years after applying filter: ", Leap_Years)


#from pymongo import MongoClient


#change the MongoClient connection string to your MongoDB database instance
c = MongoClient()
db=c.trial

result = db.restaurants.delete_many({"category": "Bar Food"})
bar_food = db.reviews.find({'category': 'Bar Food'}).count()
print(bar_food)
