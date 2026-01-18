# Working with REST APIs using requests
import requests

def run_api(url):  
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("API Call failed")
    return response.status_code

#url = "https://jsonplaceholder.typicode.com/todos/1"
#print(run_api(url))