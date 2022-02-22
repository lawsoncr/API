import requests

#Get request generates two random memes found using reddit API
#To run type py main.py

url = "https://reddit-meme.p.rapidapi.com/memes/trending"

headers = {
    'x-rapidapi-host': "reddit-meme.p.rapidapi.com",
    'x-rapidapi-key': "insert api key"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
