import team

class Battle:
    def __init__(self, player1, player2)
    self.team1 = player1 # team objects
    self.team2 = player2

    def start(self):
        var = True
        while var:
            self.get_input(self.player1)
            # player1 makes move
            # if player2 is not dead
                self.get_input(self.player2)

    def get_input(self, player):
        print("Options: ATK or SWAP")
        choice = input(player.name + " chooses: ")
        print("\n")
        player.choice = choice.lower()