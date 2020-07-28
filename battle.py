import team

class Battle:
    def __init__(self, player1, player2)
    self.team1 = player1 # team objects
    self.team2 = player2
    self.life1 = [1, 1, 1, 1, 1, 1]
    self.life2 = [1, 1, 1, 1, 1, 1]

    def start(self):
        var = True
        while var:
            self.get_input(self.player1)
            # player1 makes move
            if self.life2 != [0, 0, 0, 0, 0, 0]:
                self.get_input(self.player2)

    def get_input(self, player):
        print("Options: ATK or SWAP")
        choice = input(player.name + " chooses: ")
        print("\n")
        player.choice = choice.lower()