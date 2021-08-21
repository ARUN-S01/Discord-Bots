import requests
import random

url = "https://bing-news-search1.p.rapidapi.com/news"

querystring = {"safeSearch":"Off","textFormat":"Raw"}

headers = {
    'x-bingapis-sdk': "true",
    'x-rapidapi-key': "f98db6d05cmsh7dbb4571174d9b1p1a02e8jsn703bbabe1ae3",
    'x-rapidapi-host': "bing-news-search1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
r = list(response)
print(random.choice(r))
