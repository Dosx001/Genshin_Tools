import json

with open('missions.json') as f:
    data = json.load(f)

for region in 'Mondstadt', 'Liyue':
    new_data = {}
    for line in open(f'{region}.txt'):
        line = line[0:len(line)-1]
        if not line in data['World'][f'{region}']:
            req = {
                'Location': None,
                'Adventure Rank': None,
                'Archon': None,
                'World': None,
                'Commission': None,
                'NPC': None
                }
            new_data.update({line: req})
    data['World'][f'{region}'].update(new_data)
    data['World'][f'{region}'] = {i:data['World'][f'{region}'][i] for i in
            sorted(data['World'][f'{region}'])}

new_data = {}

for line in open('Commissions.txt'):
    line = line[0:len(line)-1]
    if not line in data['Commission']:
        req = {
            'World': None
            }
        new_data.update({line: req})
data['Commission'].update(new_data)
data['Commission'] = {i:data['Commission'][i] for i in
        sorted(data['Commission'])}

files = ['pa1.txt', 'pa2.txt', 'pa3.txt', 'c1a1.txt', 'c1a2.txt', 'c1a3.txt']
chapters = data['Archon']['Prologue']
chapters.update(data['Archon']['Chapter 1'])

for i, chapter in enumerate(chapters):
    quests = []
    for line in open(files[i]):
        line = line[0:len(line)-1]
        quests.append(line)
    data['Archon']['Prologue' if i < 3 else 'Chapter 1'][chapter].update({'quests':quests})

with open('new_missions.json', 'w') as f:
    json.dump(data, f, indent=4)
