import requests

import requests

BASE_URL = 'https://thrower-decaf-bogus.ngrok-free.dev/'

# single cards
r = requests.get(f'{BASE_URL}/cards/Lightning Bolt')
print(r.json())

r = requests.get(f'{BASE_URL}/cards/Swords to Plowshares')
print(r.json())

r = requests.get(f'{BASE_URL}/cards/Serra Angel')
print(r.json())