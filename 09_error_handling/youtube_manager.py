
import json

youtube_file = 'youtube.txt'

def load_data():
    try:
        with open(youtube_file, 'r') as file:
            test = json.load(file)          # load data from the file
            # print(type(test))               # JSON list
            return test                     
    except (FileNotFoundError, json.JSONDecodeError):
        # Initialize or reset file if not exists or empty/corrupted
        save_data_helper([])
        return []
    
def save_data_helper(videos):
    with open(youtube_file, 'w') as file:
        json.dump(videos, file)             # write data to the file

def list_all_videos(videos):
    print()
    print("*" * 80)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration:  {video['time']}")
    print("*" * 80)

def add_video(videos):
    name = input("Enter video name: ")    
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video index to update: "))
    if 0 < index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)
        print(f"Video {index} is updated")
    else:
        print("Invalid video index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter index of video to be deleted: "))
        
    if 0 < index <= len(videos):
        del videos[index-1]
        my_video = save_data_helper(videos)
        print(f"Video {index} is deleted")
        if my_video is videos:
            print(True)
        else:
            print(False)
    else:
        print("Invalid video index selected")

def main():
    videos = load_data()
    
    while True:
        print("\n Youtube Manager | Choose an Option ")
        print("1. List all videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the Application ")
        
        choice = input("Enter your choice : ")
        # print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()