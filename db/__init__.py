from pymongo import MongoClient
from config import settings

client = None
db = None


def get_db():
    """Get the MongoDB database instance."""
    global client, db
    if client is None:
        client = MongoClient(settings.mongodb_uri)
        db = client[settings.mongodb_database]
    return db


def test_connection():
    """Test if the database connection is working."""
    try:
        database = get_db()
        # The ping command is lightweight and verifies connectivity
        database.command("ping")
        return {"status": "connected", "database": settings.mongodb_database}
    except Exception as e:
        return {"status": "disconnected", "error": str(e)}