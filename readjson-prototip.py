from fuzzywuzzy import fuzz
import json

with open("domains.json", "r", encoding="utf-8") as berlin:
	veri = json.load(berlin)

with open("domains1.json", "r", encoding="utf-8") as berlinx:
        veri1 = json.load(berlinx)

target = input("Hedef").strip().casefold()

for key in veri.keys():
	benzerlik = fuzz.ratio(key, target)
	if benzerlik > 50:
		print(f"{key} {target} ile {benzerlik}% oraninda benziyor. Sonuc: {veri[key]} ")
	else:
		for key1 in veri1.keys():
			benzerlik1 = fuzz.ratio(key1, target)
			if benzerlik1 > 40:
				print(f"yedek listedeki {key1}, {target} ile {benzerlik}% oraninda benziyor. Sonuc: {veri1[key1]}")

