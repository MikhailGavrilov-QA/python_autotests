import requests
response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
              json={
                     "pokemon_id": "20565"
                   },
               headers={'Content-Type': 'application/json', 'trainer_token': 'e447d5f9b119d3bf996797514640e374'},
               timeout=5)
print(f'Code: {response.status_code}. Message: {response.text}')
response.status_code ==400