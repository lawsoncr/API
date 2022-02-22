import requests

#Get request generates two random memes found using reddit API
#To run type py main.py

url = "https://reddit-meme.p.rapidapi.com/memes/trending"

headers = {
    'x-rapidapi-host': "reddit-meme.p.rapidapi.com",
    'x-rapidapi-key': "84a8eeab97mshd52f4f6edf81a07p1ce7fbjsn40548363d4e1"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)