import api

class Team:
    def __init__(self):
        self.pokemon = {}

    def add_pokemon(self, names):
        for name in names:
            self.pokemon.update({name: api.get_pokemon_data(name)})

    def remove_pokemon(self, name):
        self.pokemon.pop(name)

    def get_pokemon(self):
        return self.pokemon