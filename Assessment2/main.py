import json

with open("ex5.json", "r") as file:
    ex5 = json.load(file)

new_batter = {"type": "Tea"}
ex5[0]["batters"]["batter"].append(new_batter)


with open("ex5.json", "w") as file:
    json.dump(ex5, file, indent = 4)

print("batter added to json")
