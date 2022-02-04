'get pokemon data from web and save to file'

def main():
    'read pokemon data from web and save to file'
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    response_json = response.json()
    pokemon_list = response_json['results']
    for pokemon in pokemon_list:
        pokemon_name = pokemon['name']
        pokemon_url = pokemon['url']
        pokemon_response = requests.get(pokemon_url)
        pokemon_response_json = pokemon_response.json()
        pokemon_data = pokemon_response_json
        with open(pokemon_name + '.json', 'w') as f:
            json.dump(pokemon_data, f)
    print('Done!')
    
if __name__ == '__main__':
    main()
