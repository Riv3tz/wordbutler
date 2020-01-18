import requests
import json

u = "https://api.datamuse.com"
par = "/words?rel_rhy="
f = input("Enter a word")
f = u + par + f 
r = requests.get(url = f)

data = r.json()

def disp():
    words = [i['word'] for i in data]
    print(type(words))
    print(', '.join(words))

disp()
