import os
from pprint import pprint
import bson
from dotenv import load_dotenv
import pymongo
# Load config from a .env file:
load_dotenv(verbose=True)
#MONGODB_URI = os.environ["MONGODB_URI"]
# Connect to your MongoDB cluster:
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Get a reference to the "sample_mflix" database:
#db = client["zengap"]
# Get a reference to the "movies" collection:
mydb = client['sample']
mycol = mydb["movies"]


pipeline = [
   {
      "$match": {
         "device_id": "SSBAG11KN"
      }
   },


   {
      "$sort": {
         "consumption": pymongo.ASCENDING
      }
   },
]

stage_limit_1 = { "$limit": 1 }

l=[]
results = mycol.aggregate(pipeline)
for movie in results:
   """ a = movie["consumption"]
    print(a)
    l.append(a)

    n = len(l)
print("n",l[n-1])
if ((l[n-1]<l[n-2]) | (l[n-1]<0)):

    del l[n-1]

print(l)"""
   print(movie)
   print(movie["consumption"])

#   mydb.movies.remove({"consumption":47449})
   if ({'consumption':{ "$gt":movie['consumption']}}):
      #if mydb.college.remove("consumption"< movie["consumption"]):
         print("ok")

   elif ({'consumption'== movie['consumption']}):

         print("not ok")

   elif ({'consumption':{ "$lt":1}}):
         print("not ok")
   """    
   query = {"consumption":{"$lt":1500}}
   #query = {"consumption":47449}
   mycol.delete_one(query)"""
print(movie)
