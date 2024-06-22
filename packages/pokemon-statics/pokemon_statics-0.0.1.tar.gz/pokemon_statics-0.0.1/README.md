# Pokemon Statics

'pokemon statics' is a library with operate with pokeapi.co to get average height and average weight of egg_groups of pokemons.

## Simple operations:

### 1. Method get_egg_groups()
Returns a list with the names of each egg_group of pokemons.

### 2. Method get_average_height()
Returns the average height of each egg_group of pokemons.

### 3. Method get_average_weight()
Returns the average weight of each egg_group of pokemons.


## Installation with pip:
`pip install pokemon_statics`

## Requirements:
    You need to install the following python libraries:
    - pip
    - pytest
    - sqlalchemy
    - aiohttp
    - pandas

## Quickstart:
After installation, run the following code from anywhere:
````
from pokemon_statics.package_two import gets_methods as gm

# returns 8
result_get_egg_groups = get_egg_groups()

result_get_egg_groups = get_average_height(egg_group_name)

result_get_average_weight = get_average_weight(egg_group_name)
````

## Run tests:
requires the installation of the 'pytest' library before running the tests. Then, having the terminal located in the project folder, run the following command:
`pytest`