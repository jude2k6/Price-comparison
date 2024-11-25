import json,os
from mp_scrape import scrape_mp
from pworks_scrape import scrape_pworks
import datetime


base_path = os.path.dirname(__file__)

with open(base_path+"/index.json", "r") as f:
    index = json.load(f)
    
#date
date = datetime.date.today()

index["date"].append(str(date))
#my protein
prices = scrape_mp()
print(f"return {prices}")
protein_price,creatine_price = prices
index["protein"]["price"]["mp"].append(protein_price)
index["creatine"]["price"]["mp"].append(creatine_price)




#protein works
prices = scrape_pworks()
print(f"return {prices}")
protein_price,creatine_price = prices
index["protein"]["price"]["pworks"].append(protein_price)
index["creatine"]["price"]["pworks"].append(creatine_price)


with open(base_path+"/index.json","w") as f:
    json.dump(index, f,indent = 4)