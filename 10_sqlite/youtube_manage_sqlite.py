import sqlite3

# Create "youtube_manager.db" file IF NOT EXISTS, otherwise point to it
connection = sqlite3.connect("youtube_manager.db")

# Create cursor object
cursor = connection.cursor()

# Create "youtube_videos" table in SQLite database using cursor object
cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS youtube_videos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL
                )               
''')

def load_all_files():
    print("List of all videos")
    cursor.execute("SELECT * FROM youtube_videos")
    rows = cursor.fetchall()
    if not rows:
        print([])
    else:
        print('*' * 50)
        for row in rows:
            print(row)
        print('*' * 50)
        

def add_videos():
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    cursor.execute("INSERT INTO youtube_videos(name, time) VALUES (?,?)", (name, time))
    connection.commit()
    print("New video is added")
    
    
def update_videos():
    vid_id = int(input("Enter video id to be updated: "))
    name = input("Enter new video name: ")
    time = input("Enter new video time: ")
    cursor.execute("UPDATE youtube_videos SET name=?, time=? WHERE id=?", (name, time, vid_id))
    connection.commit()
    print(f"Video {vid_id} is updated successfully")

def delete_videos():
    vid_id = int(input("Enter video id to be updated: "))
    cursor.execute("DELETE FROM youtube_videos WHERE id=?", (vid_id, ))
    connection.commit()
    print(f"Video {vid_id} is deleted successfully")

def main():
    while True:
        print("\n Youtube Manager | Choose an Option ")
        print("1. List all videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the Application ")
        
        choice = input("Enter your choice : ")
        
        match choice:
            case '1':
                load_all_files()
            case '2':
                add_videos()
            case '3':
                update_videos()
            case '4':
                delete_videos()
            case '5':
                break
            case _:
                print("Invalid choice")
      
    connection.close()  
        

if __name__ == "__main__":
    main()