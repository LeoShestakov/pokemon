import team

class Battle:
    options = ["ATK"]
    def __init__(self, team1, team2):
        self.team1 = team1.get_team()
        self.team2 = team2.get_team()
        self.active = True

    def gameplay(self):
        self.start()
        while self.active:
            if self.speed(self.pokemon1, self.pokemon2):
                self.attack(self.pokemon1, self.pokemon2)
                if self.pokemon2.alive:
                    self.attack(self.pokemon2, self.pokemon1)
                else:
                    self.team2.pop(self.pokemon2)
                    if self.team2.length > 0:
                        print("SWAP")
            else:
                self.attack(self.pokemon2, self.pokemon1)
                if self.pokemon1.alive:
                    self.attack(self.pokemon1, self.pokemon2)
                else:
                    self.team1.pop(self.pokemon1)
                    if self.team1.length > 0:
                        print("SWAP")

    def start(self):
        self.pokemon1 = self.team1[0]
        self.pokemon2 = self.team2[0]

    def attack(self, attacker, target):
        damage = 42 * (attacker.getStats()['attack'] / target.getStats()['defense']) * 80 # 80 == Power
        damage = (damage / 50) + 2
        target.damage(damage)

    def speed(self, pokemon1, pokemon2):
        return pokemon1.getStats()['speed'] >= pokemon2.getStats()['speed']
    
    def swap(self, team):
        input()