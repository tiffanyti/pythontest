"""database"""
import pymongo

MYCLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
MYDB = MYCLIENT["mydatabase"]
MYCOL = MYDB["customers"]

# i = 0
# for record in MYCOL.find():
#         i += 1
#         record.update({'number' : i})
#         print(record)

try:
    pymongo.MongoClient()
    print("Connected successfully to database")
except:
    print("Could not connect to MongoDB")

print("\n", 22*"=", "\n")

print('list of databases :', MYCLIENT.list_database_names())

print("\n", 22*"=", "\n")
