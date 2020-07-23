import api

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

    def get_picture(self, name):
        image = self.pokemon[name]['sprites']['front_default']
        if image is None:
            return "https://i0.wp.com/www.alphr.com/wp-content/uploads/2016/07/whos_that_pokemon.png?resize=1280%2C960&ssl=1"
        return image
