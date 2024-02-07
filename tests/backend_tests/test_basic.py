import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers_by_level():
    """
    KTI-1. Get the list of trainers sorted by level
    """
    response = requests.get(url=f'{URL}/trainers', params = {'level': 3}, timeout = 5)
    assert response.status_code == 200, 'Unexpected status code'

CASES = [
     (4655, 'Zimbabve', 'Pupsen'),
     (4657, 'Moscow', 'Serge'),
]

@pytest.mark.parametrize('id, city, trainer_name', CASES)
def test_get_trainers_by_id(id, city, trainer_name):
    """
    KTI-2. Get the list of trainers sorted by id
    """
    response = requests.get(url=f'{URL}/trainers', params = {'trainer_id': id}, timeout = 5)
    assert response.json()['city'] == city, ''
    assert response.json()['trainer_name'] == trainer_name, ''