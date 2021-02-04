from bson.objectid import ObjectId
from mongo.base import mongodb


collection = mongodb["Classrooms"]


def get_classroom(document_id):
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data


def get_multiple_data():
    data = collection.find()
    return list(data)


def add_classroom(data):
    x = collection.insert_one(data)
    return x #returned onject contains inserted id, acknowledgement