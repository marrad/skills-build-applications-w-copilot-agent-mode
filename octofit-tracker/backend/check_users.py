from pymongo import MongoClient

# MongoDB connection details
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
DB_NAME = 'octofit_db'
COLLECTION_NAME = 'octofit_tracker_user'

def check_users():
    try:
        # Connect to MongoDB
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client[DB_NAME]
        users_collection = db[COLLECTION_NAME]

        # Count the number of documents in the collection
        user_count = users_collection.count_documents({})
        print(f"Number of users in the collection: {user_count}")

        # Fetch and print the first 5 users if any exist
        if user_count > 0:
            users = users_collection.find().limit(5)
            for user in users:
                print(user)
        else:
            print("The users collection is empty.")

        # List all collections in the database
        collections = db.list_collection_names()
        print(f"Collections in the database: {collections}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_users()
