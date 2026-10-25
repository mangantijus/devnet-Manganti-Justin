import requests
import random

pokemon_list = ['https://pokeapi.co/api/v2/pokemon/10',
                'https://pokeapi.co/api/v2/pokemon/5',
                'https://pokeapi.co/api/v2/pokemon/20',
                'https://pokeapi.co/api/v2/pokemon/6',
                'https://pokeapi.co/api/v2/pokemon/7']

# Pick one random Pokemon URL from the list
url = random.choice(pokemon_list)

# Request the data (handle network errors)
try:
    pokemon = requests.get(url, timeout=10)
except requests.exceptions.RequestException:
    print("Network error. Please check your internet and try again.")
    exit()

# Check the HTTP status before processing the data
if pokemon.status_code != 200:
    print("Error: could not get Pokemon data. Status code:", pokemon.status_code)
    exit()

# Process the JSON
answer = pokemon.json()
name = answer["name"]
height = answer["height"]
weight = answer["weight"]

# Show clues (without the name)
print("WHO'S THAT POKEMON?")
print("Height:", height)
print("Weight:", weight)

# Game: 3 attempts
attempts = 3
while attempts > 0:
    guess = input("Your guess: ").lower().strip()

    # Invalid name (empty or has numbers/symbols)
    if not guess.replace("-", "").isalpha():
        print("Invalid name. Use letters only.")
        continue

    if guess == name:
        print("Correct! It's", name.capitalize(), "- You win!")
        break

    attempts -= 1
    if attempts > 0:
        print("Wrong! Attempts left:", attempts)
else:
    print("You lost! The Pokemon was", name.capitalize())
