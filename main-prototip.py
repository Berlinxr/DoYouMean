from fuzzywuzzy import fuzz
import json
import requests
from ayarlar import * # api key, cx key

eslesme = False

with open("domains.json", "r", encoding="utf-8") as berlin:
	veri = json.load(berlin)

with open("domains1.json", "r", encoding="utf-8") as berlinx:
        veri1 = json.load(berlinx)

with open("counter.json", "r", encoding="utf-8") as berlinxr:
	counters = json.load(berlinxrf)

target = input("Hedef: ").strip().casefold()
api = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX_KEY}&q={target}"
apidata = requests.get(api).json()
link1 = apidata["items"][0]["link"]
domain = link1.split("/")[2] 

for key in veri.keys():
	benzerlik = fuzz.ratio(key, target)
	if benzerlik > 50:
		print(f"{key} {target} ile {benzerlik}% oraninda benziyor. Sonuc: {veri[key]} ")
		eslesme = True 
		break

if not eslesme:
	for key1 in veri1.keys():
		benzerlik1 = fuzz.ratio(key1, target)
		if benzerlik1 > 40:
			print(f"yedek listedeki {key1}, {target} ile {benzerlik}% oraninda benziyor. Sonuc: {veri1[key1]}")
			eslesme = True
			break

if not eslesme:
	print(f"{domain}")
	veri1[target] = domain
	with open("domains1.json", "w", encoding="utf-8") as berlinxr:
		json.dump(veri1, berlinxr, indent=4)