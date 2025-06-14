import requests

def fetch_cat_by_id():
    url = "https://api.freeapi.app/api/v1/public/cats/12"
    response = requests.get(url)
    response_json = response.json()
    
    if response_json["success"] and "data" in response_json:
        cat_data = response_json["data"]
        cat_id = cat_data["id"]
        name = cat_data["name"]
        description = cat_data["description"]
        return cat_id, name, description
    else:
        raise Exception("No cats are found")
    
def fetch_cat_api():
    url = "https://api.freeapi.app/api/v1/public/cats?query=sociable&page=1&limit=10"
    response = requests.get(url)
    response_json = response.json()
    
    if response_json["success"] and "data" in response_json:
        cat_data = response_json["data"].get("data", [])
        if not cat_data:
            raise Exception("No cats are found in cat_data")
        first_cat = cat_data[0]
        return first_cat["id"], first_cat["name"], first_cat["description"]
    else:
        raise Exception("No cats are found")
    
    
def main():
    try:
        cat_id, cat_name, cat_description = fetch_cat_api()
        print(f"{cat_id}: {cat_name}")
        print(f"Description: {cat_description}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()