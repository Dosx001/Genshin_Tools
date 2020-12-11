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

with open('new_missions.json', 'w') as f:
    json.dump(data, f, indent=4)
