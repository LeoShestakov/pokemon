import api
from enum import Enum


class Sprite(Enum):
    BACK = 0
    FRONT = 1


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.json = api.get_pokemon_data(name)
        self.stats = self.__statInit()
        self.health = self.stats['hp']
        self.alive = self.health > 0
        self.inPlay = False

    def __statInit(self):
        base_stats = self.json['stats']
        keys = ["hp", "attack", "defense",
                "special-attack", "special-defense", "speed"]
        stats_list = []
        for stats in base_stats:
            val = (2 * stats['base_stat'] + 31)
            if stats['stat']['name'] == 'hp':
                val += 110
            else:
                val += 5
            stats_list.append(val)
        return dict(zip(keys, stats_list))

    def battle_image(self, name, sprite):
        image = ""
        if sprite == Sprite.FRONT:
            image = self.pokemon[name]['sprites']['front_default']
        else:
            image = self.pokemon[name]['sprites']['back_default']

        if image is None:
            return "https://vignette.wikia.nocookie.net/super-arc-bros-brawl/images/6/62/MissingNo.png"
        return image

    def getInfo(self):
        return self.json

    def damage(self, damage):
        if damage < self.health:
            self.health -= damage
        else:
            self.health = 0
            self.alive = False

    def inPlay(self):
        self.inPlay = True

    def outOfPlay(self):
        self.outOfPlay = False

    def getStats(self):
        return self.stats
