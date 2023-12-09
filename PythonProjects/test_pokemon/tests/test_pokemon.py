import requests
import pytest

def test_ger_trainers():
    response = requests.get(url='https://api.pokemonbattle.me:9104/trainers', 
     headers={'Content-Type': 'application/json', 'trainer_token': 'e447d5f9b119d3bf996797514640e374'},
     timeout=5, params={'trainer_id':3345})
    print(f'Code: {response.status_code}. Message: {response.text}')
    assert response.status_code == 200