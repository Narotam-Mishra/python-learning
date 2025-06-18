
import sys
from pymongo import MongoClient
from bson import ObjectId
from config import Config

# validate configuration before proceeding
try:
    Config.validate_config()
except ValueError as e:
    print(f"Configuration Error: {e}")
    sys.exit(1)

# initialize MongoDB connection using config
client = MongoClient(Config.MONGODB_URI)
db = client[Config.DATABASE_NAME]
videos_data_collection = db[Config.COLLECTION_NAME]

# client = MongoClient("your_mongodb_connection_string")
# print("Client:", client)

# db = client["ytmanager"]
# videos_data_collection = db["videos"]
# print("collection_name:", videos_data_collection)

def test_connection():
    """Test MongoDB connection"""
    try:
        # Test the connection
        client.admin.command('ping')
        print("✅ MongoDB connection successful!")
        return True
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        return False

def list_videos():
    for video in videos_data_collection.find({}):
        print(f"Id: {video["_id"]}, Name: {video["name"]}, Duration: {video["time"]}")

def add_video(name, time):
    videos_data_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    videos_data_collection.update_one(
        {'_id': ObjectId(video_id)}, 
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    videos_data_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    # test mongodb connection before starting
    if not test_connection():
        print("Please check your MongoDB connection settings and try again.")
        return
    
    while True:
        print("\n Youtube manager with mongodb")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video_id to be updated: ")
            name = input("Enter video name to be updated: ")
            time = input("Enter video time to be updated: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video_id to be deleted: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice!!")
            

if __name__ == "__main__":
    main()