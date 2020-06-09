"""database"""
import pymongo

MYCLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
MYDB = MYCLIENT["mydatabase"]
MYCOL = MYDB["customers"]

try:
    pymongo.MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

print(MYCLIENT.list_database_names())

COLL = MYCOL.find()
for record in COLL:
    print(record)

print(__name__)
