import requests
import json

'''
A module for fetching data from the Pokemon API and saving it to a JSON file 
called "poke_data.json".

To generate the JSON file, run `python3 fetch.py` from this project's root directory.
'''

poke_list = []
for ind in range(1, 152):
    link = 'https://pokeapi.co/api/v2/pokemon-species/{}/'.format(ind)
    print('Fetching from', link, '...')
    fetched = requests.get(link)

    data = fetched.text
    results = json.loads(data)
    poke_list.append({
        'name': results['name'],
        'color': results['color']['name'],
        'shape': results['shape']['name'],
        'base_happiness': results['base_happiness']
    })

with open('../static/poke_data.json', 'w+') as f:
    json.dump(poke_list, f)
