from databases import Database
from dotenv import load_dotenv
import sqlalchemy
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

db = Database(os.environ["GS_DATABASE_URL"])

metadata = sqlalchemy.MetaData()