from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

connection = pymongo.MongoClient("mongodb+srv://kp:kp@cluster0.lx8yo.mongodb.net/")
mongodb = connection["Enrolled"]