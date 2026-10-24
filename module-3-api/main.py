import requests
import random


pokemon_list = [ 'https://pokeapi.co/api/v2/pokemon/10',
                'https://pokeapi.co/api/v2/pokemon/5',
                'https://pokeapi.co/api/v2/pokemon/20',
                'https://pokeapi.co/api/v2/pokemon/6',
                'https://pokeapi.co/api/v2/pokemon/7'
            
]
    pokemon = requests.get(pokemon_list)
    answer = pokemon.json()






