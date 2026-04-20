import requests

def get_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data=response.json()
        for post in data[:5]:
            print(post["title"])

    else:
        print("Failed to fetch data")

get_data()
