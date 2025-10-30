import requests

url = "https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={CX_KEY}&q={q}"
veri = requests.get(url).json()

link1 = data["items"][0]["link"]
domain = link1.split("/")[2] 
print(domain)
