rivers = {
    'nile': 'egypt',
    'volga': 'russia',
    'amazon': 'usa',
}

for k, v in rivers.items():
    print('The ' + k + ' runs through ' + v)

for k in rivers.keys():
    print('river ' + k)

for v in rivers.values():
    print('country ' + v)