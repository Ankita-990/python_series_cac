import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    # print(f"{response}, type is {type(response)}")        # type = Class
    response_data = response.json()                     # Convert into json format
    
    if response_data["success"] and "data" in response_data:
        user_data = response_data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch data")
        
    
def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"Username = {username}, location = {country}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()