import requests
print("** Welcome to pokeapi client **")

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if(response.status_code==200):
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retreive data {response.status_code}")



pokemon_name="typhlosion"      #Examples: pikachu
pokemon_info = get_pokemon_info(pokemon_name)

if(pokemon_info):
    print(f"name: {pokemon_info["name"].capitalize()}")
    print(f"id: {pokemon_info["id"]}")
    print(f"height: {pokemon_info["height"]}")
    print(f"weight: {pokemon_info["weight"]}")
