import pymongo
from bson.objectid import ObjectId


client = pymongo.MongoClient("mongodb+srv://kp:kp@cluster0.lx8yo.mongodb.net/")
db = client["Enrolled"]
print(db.test)
collection = db["Classrooms"]


def get_single_data(document_id):
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data

def get_multiple_data():
    data = collection.find()
    return list(data)

def insert(data):
    x = collection.insert_one(data)
    return x

i = input()
data = {
    "name": "hello",
    "value": "hello"
}
x = insert(data)
print(x.inserted_id)