from random import randrange as rand
import json

with open('missions.json') as f:
    data = json.load(f)

new = {}
for chapter in data['Archon']:
    for mission in data['Archon'][chapter]:
        new.update({mission:True if rand(0, 2) == 1 else False})

for region in data['World']:
    for mission in data['World'][region]:
        new.update({mission:True if rand(0, 2) == 1 else False})

for mission in data['Commission']:
    new.update({mission:True if rand(0, 2) == 1 else False})

with open('new.json', 'w') as f:
    json.dump(new, f, indent = 4)
