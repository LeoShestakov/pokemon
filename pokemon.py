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

    def battle_image(self, sprite):
        image = ""
        if sprite == Sprite.FRONT:
            image = self.json['sprites']['front_default']
        else:
            image = self.json['sprites']['back_default']

        if image is None:
            return "https://vignette.wikia.nocookie.net/super-arc-bros-brawl/images/6/62/MissingNo.png"
        return image

    def getInfo(self):
        info = {}
        info.update({'name': self.name})
        info.update({'stats': self.stats})
        info.update({'type': self.getType()})
        info.update({'sprites': {
                                'front': self.battle_image(Sprite.FRONT),
                                'back': self.battle_image(Sprite.BACK)
                                }})
        return info

    def getType(self):
        data = self.json['types']
        ans = []
        for poke_type in data:
            ans.append(poke_type['type']['name'].capitalize())
        return ans

    def damage(self, damage):
        if damage < self.health:
            self.health -= damage
        else:
            self.health = 0
            self.alive = False

    def swapPlay(self):
        self.inPlay = not self.inPlay

    def getStats(self):
        return self.stats

    def isAlive(self):
        return self.alive
