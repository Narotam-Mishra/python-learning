
import sqlite3

# establish connection to SQLite database
# creates 'youtube_videos.db' file if it doesn't exist
conn = sqlite3.connect('youtube_videos.db')

# create cursor object to execute SQL commands
cursor = conn.cursor()

# create the videos_data table if it doesn't already exist
# table structure: id (auto-increment primary key), name (video title), time (video duration)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos_data(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL      
    )
''')

def list_videos():
    """
    Retrieve and display all videos from the database.
    Fetches all records from videos_data table and prints them.
    """
    cursor.execute("SELECT * FROM videos_data")
    videos = cursor.fetchall()

    if videos:
        print("\n--- All Videos ---")
        for row in videos:
            print(f"ID: {row[0]}, Name: {row[1]}, Duration: {row[2]}")
    else:
        print("No videos found in the database!!")

def add_video(name, time):
    """
    Add a new video record to the database.
    
    Args:
        name (str): The name/title of the video
        time (str): The duration of the video
    """
    cursor.execute("INSERT INTO videos_data (name, time) VALUES (?, ?)", (name, time))
    print(f"Video '{name}' added successfully!")

    # save changes to database
    conn.commit()

def update_video(video_id, new_name, new_time):
    """
    Update an existing video record in the database.
    
    Args:
        video_id (str): The ID of the video to update
        new_name (str): The new name/title for the video
        new_time (str): The new duration for the video
    """
    # check if video exists before updating
    cursor.execute("SELECT * FROM videos_data WHERE id = ?", (video_id,))
    if cursor.fetchone():
        cursor.execute("UPDATE videos_data SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
        # save changes to database
        conn.commit()  
        print(f"Video ID {video_id} updated successfully!")
    else:
        print(f"Video with ID {video_id} not found.")

def delete_video(video_id):
    """
    Delete a video record from the database.
    
    Args:
        video_id (str): The ID of the video to delete
    """
    # check if video exists before deleting
    cursor.execute("SELECT * FROM videos_data WHERE id = ?", (video_id,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM videos_data WHERE id = ?", (video_id,))
        # save changes to database
        conn.commit()  
        print(f"Video ID {video_id} deleted successfully!")
    else:
        print(f"Video with ID {video_id} not found.")   

def main():
    """
    Main function that runs the interactive menu system.
    Provides a command-line interface for managing YouTube videos.
    """
    while True:
        # Display menu options
        print("\n Youtube manager app with sqlite db")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video Id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video Id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice!!")
    
    conn.close()
    print("Database connection closed!!")

if __name__ == "__main__":
    main()