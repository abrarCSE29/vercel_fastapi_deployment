from pymongo import MongoClient
from config import MONGODB_URI, MONGODB_DATABASE

client = None
db = None


def get_db():
    """Get the MongoDB database instance."""
    global client, db
    if client is None:
        client = MongoClient(MONGODB_URI)
        db = client[MONGODB_DATABASE]
    return db


def test_connection():
    """Test if the database connection is working."""
    try:
        database = get_db()
        # The ping command is lightweight and verifies connectivity
        database.command("ping")
        return {"status": "connected", "database": MONGODB_DATABASE}
    except Exception as e:
        return {"status": "disconnected", "error": str(e)}
