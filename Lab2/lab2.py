import json


with open('RomeoAndJuliet.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

characters = set()
mx = 0
maxcharacter= ""



for act in data["acts"]:
    for scene in act["scenes"]:
        action = scene["action"]
        for charwords in action:
            characters.add(charwords["character"])
            words = charwords["says"]
            l = 0
            for w in words:
                l = l + len(w)
            if l > mx:
                mx = l
                maxcharacter = charwords["character"]

            
print(maxcharacter + ": " + str(mx))
print(sorted(characters))
print(len(characters))
        

#create a new file
json_file = open('my.json', 'w')
json_file.write(json.dumps({"fruits" : [{"name" : "apple","type" : "citrus"},{"name" : "orange","type" : "dunno"}]}, sort_keys=True, indent=4))

#print(json.dumps({"fruits" : [{"name" : "apple","type" : "citrus"},{"name" : "orange","type" : "dunno"}]}, sort_keys=True, indent=4))
json_file.close()
