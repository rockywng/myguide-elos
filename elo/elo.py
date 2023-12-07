import random

class Player:
    def __init__(self, current_elo):
        self.elo = current_elo
    
    def get_elo(self):
        return self.elo
    
    def update_elo(self, new_elo):
        self.elo = new_elo
    
    def show_elo(self):
        print('Current Elo: ' + str(self.elo))

def head_to_head(player1, player2, winner):
    p1 = 1.0 * 1.0 / (1 + 1.0 * pow(10, 1.0 * (player1.get_elo() - player2.get_elo()) / 400))
    p2 = 1.0 - p1
    if winner == 0:
        # player1 wins
        player1_new_rating = player1.get_elo() + k * (1 - p1)
        player2_new_rating = player2.get_elo() + k * (0 - p2)
    else:
        player1_new_rating = player1.get_elo() + k * (0 - p1)
        player2_new_rating = player2.get_elo() + k * (1 - p2)
    
    player1.update_elo(player1_new_rating)
    player2.update_elo(player2_new_rating)