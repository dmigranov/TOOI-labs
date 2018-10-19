import json


#with open('RomeoAndJuliet.json') as f:
    #data = json.load(f)

with open('RomeoAndJuliet.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())


#characters = set(item['character'] for item in data.values())
characters = set()

for act in data["acts"]:
    for scene in act["scenes"]:
        action = scene["action"]
        for words in action:
            #print(words["character"])
            characters.add(words["character"])

print(sorted(characters))
        
