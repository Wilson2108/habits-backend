from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

habits_collection = db["habits"]
habit_logs_collection = db["habit_logs"]


#### Check
def ping_db():
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully")
    except Exception as e:
        print("MongoDB connection error:", e)