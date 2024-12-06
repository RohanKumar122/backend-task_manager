from pymongo import MongoClient, ASCENDING
from dotenv import load_dotenv
import os


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set. Please check your .env file.")

DB_NAME = "task_manager"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
tasks_collection = db.tasks

tasks_collection.create_index([("created_at", ASCENDING)])
tasks_collection.create_index([("due_date", ASCENDING)])
