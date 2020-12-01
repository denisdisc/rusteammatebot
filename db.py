from pymongo import MongoClient
from config import MONGO_PASS, MONGO_LOGIN, MONGO_DB


client = MongoClient(
    f"mongodb+srv://{MONGO_LOGIN}:{MONGO_PASS}@cluster0.pqa1m.mongodb.net/test"
)
db = client[MONGO_DB]

def get_or_create_user(db, effective_user, chat_id):
    user = db.users.find_one({"user_id": effective_user.id})
    if not user:
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "username": effective_user.username,
            "chat_id": chat_id
        }
        db.users.insert_one(user)
    return user
