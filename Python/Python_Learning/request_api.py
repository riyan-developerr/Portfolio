""" 
I was getting error none type object is not subcriptable 
it was because i was not checking whether the data is retrived with status code 200 or just returned none object becaue in else statement i 
did not returned anything 

if pokemon_info:
    print(f"name: {pokemon_info["name"]}")
    # print(f"abilities: {pokemon_info["abilities"][0]["ability"]["name"]}")
    # print(f"abilities: {pokemon_info["abilities"][1]["ability"]["name"]}")
"""


import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Data is not retreived \nstatus code:{response.status_code}")

pokemon_name = "pikachu"

pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"name: {pokemon_info["name"].capitalize()}")
    print(f"id: {pokemon_info["id"]}")
    print(f"height: {pokemon_info["height"]}")
    # print(f"abilities: {pokemon_info["abilities"][0]["ability"]["name"]}")
    # print(f"abilities: {pokemon_info["abilities"][1]["ability"]["name"]}")