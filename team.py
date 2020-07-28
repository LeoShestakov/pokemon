import api
import numpy as np
from enum import Enum


class Sprite(Enum):
    BACK = 0
    FRONT = 1


### A Pokemon Types Table Plot In Python
### Seaborn Approach:
# References:
# https://stackoverflow.com/questions/33158075/custom-annotation-seaborn-heatmap
# https://stackoverflow.com/questions/40734343/artificial-tick-labels-for-seaborn-heatmaps
# Pokemon Type Table Reference: https://img.pokemondb.net/images/typechart.png

pokemon_types = {"Normal" : 0, "Fire" : 1, "Water" : 2, "Electric" : 3, "Grass" : 4, "Ice" : 5,
                 "Fighting" : 6, "Poison" : 7, "Ground" : 8, "Flying" : 9, "Psychic" : 10,
                 "Bug" : 11, "Rock" : 12, "Ghost" : 13, "Dragon" : 14, "Dark" : 15, "Steel" : 16, "Fairy" : 17}

# A 2 Dimenstional Numpy Array Of Damage Multipliers For Attacking Pokemon:

damage_array = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                    [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
                    [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
                    [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
                    [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
                    [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
                    [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
                    [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
                    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
                    [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
                    [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
                    [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
                    [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
                    [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]])
class Team:
    def __init__(self):
        self.pokemon = {}
        self.poke_names = []

    def add_pokemon(self, names):
        for name in names:
            self.poke_names.append(name)
            self.pokemon.update({name: api.get_pokemon_data(name)})

    def get_names(self):
        return self.poke_names

    def remove_pokemon(self, name):
        self.pokemon.pop(name)

    def get_pokemon(self):
        return self.pokemon

    def get_type(self, name):
        data = self.pokemon[name]['types']
        ans = []
        for poke_type in data:
            ans.append(poke_type['type']['name'].capitalize())
        return ans

    def get_types(self):
        types = []
        for mon in self.pokemon:
            types.extend(self.get_type(mon))
        return list(set(types))

    def get_weaknesses(self):
        my_types = self.get_types()
        weaknesses = []
        keys = list(pokemon_types.keys())
        for poke_type in my_types:
            def_index = pokemon_types[poke_type]
            for i in range(len(damage_array)):
                if damage_array[i][def_index] == 2:
                    weaknesses.append(keys[i])
        weaknesses = list(set(weaknesses))
        return weaknesses

    def get_unchecked(self):
        weaknesses = self.get_weaknesses()
        countered = []
        for weakness in weaknesses:
            for type in self.get_types():
                atk_index = pokemon_types[type]
                def_index = pokemon_types[weakness]
                if damage_array[atk_index][def_index] == 2:
                    countered.append(weakness)
                    break
        for not_weak in countered:
            weaknesses.remove(not_weak)
        return weaknesses

    def get_picture(self, name):
        image = self.pokemon[name]['sprites']['front_default']
        if image is None:
            return "https://i0.wp.com/www.alphr.com/wp-content/uploads/2016/07/whos_that_pokemon.png?resize=1280%2C960&ssl=1"
        return image

    def battle_image(self, name, Sprite):
        image = ""
        if Sprite == Sprite.FRONT:
            image = self.pokemon[name]['sprites']['front_default']
        else:
            image = self.pokemon[name]['sprites']['back_default']

        if image is None:
            return "https://vignette.wikia.nocookie.net/super-arc-bros-brawl/images/6/62/MissingNo.png"
        return image

    def battle_stat(self, name):
        base_stats = self.pokemon[name]['stats']
        keys = ["hp", "attack", "defense", "special-attack", "special-defense", "speed"]
        stats_list = []
        for stats in base_stats:
            stats_list.append(stats['base_stat'])
        return dict(zip(keys, stats_list))
        
