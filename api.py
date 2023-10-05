import requests 
base_url = "https://api.deezer.com/https:/deezer.page.link/PCfwyvu8PGTsteSEA"

def get_data(api_endpoint) : 
    url = f"{base_url}/{api_endpoint}"
    response = requests.get(url) 

    if response.status_code == 200: 
        return response.json() 
    else: 
        print(f"Error: {response.statis_code}")
        return None 
