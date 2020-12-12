import json

with open('missions.json') as f:
    data = json.load(f)

new_data = {}

for line in open('Mondstadt.txt'):
    line = line[0:len(line)-1]
    if not line in data['World']['Mondstadt']:
        req = {
            'Location': None,
            'Adventure Rank': None,
            'Archon': None,
            'World': None,
            'Commission': None,
            'NPC': None
            }
        new_data.update({line: req})
data['World']['Mondstadt'].update(new_data)
data['World']['Mondstadt'] = {i:data['World']['Mondstadt'][i] for i in
        sorted(data['World']['Mondstadt'])}

new_data = {}

for line in open('Liyue.txt'):
    line = line[0:len(line)-1]
    if not line in data['World']['Liyue']:
        req = {
            'Location': None,
            'Adventure Rank': None,
            'Archon': None,
            'World': None,
            'Commission': None,
            'NPC': None
            }
        new_data.update({line: req})
data['World']['Liyue'].update(new_data)
data['World']['Liyue'] = {i:data['World']['Liyue'][i] for i in
        sorted(data['World']['Liyue'])}

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

quests = []
for line in open('pa1.txt'):
    line = line[0:len(line)-1]
    quests.append(line)
data['Archon']['Prologue']['The Outlander Who Caught the Wind'].update({'quests':quests})

quests = []
for line in open('pa2.txt'):
    line = line[0:len(line)-1]
    quests.append(line)
data['Archon']['Prologue']['For a Tomorrow Without Tears'].update({'quests':quests})

quests = []
for line in open('pa3.txt'):
    line = line[0:len(line)-1]
    quests.append(line)
data['Archon']['Prologue']['Song of the Dragon and Freedom'].update({'quests':quests})

quests = []
for line in open('c1a1.txt'):
    line = line[0:len(line)-1]
    quests.append(line)
data['Archon']['Chapter 1']['Of the Land Amidst Monoliths'].update({'quests':quests})

quests = []
for line in open('c1a2.txt'):
    line = line[0:len(line)-1]
    quests.append(line)
data['Archon']['Chapter 1']['Farewell, Archaic Lord'].update({'quests':quests})

quests = []
for line in open('c1a3.txt'):
    line = line[0:len(line)-1]
    quests.append(line)
data['Archon']['Chapter 1']['A New Star Approaches'].update({'quests':quests})

with open('new_missions.json', 'w') as f:
    json.dump(data, f, indent=4)
