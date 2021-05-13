import random

class Shuffle:
    """Comment"""

    def __init__(self):
        """Comment"""

        self.deck = list(range(1,14))
        self.old_card = 7
        self.new_card = 7

    def get_card(self, card_type):
        """Comment"""

        if card_type == "old":
            return self.old_card
        return self.new_card

    def shuffle_deck(self):
        """Comment"""

        self.old_card = self.new_card
        self.new_card = random.choice(self.deck)

        while self.old_card == self.new_card:
            self.new_card = random.choice(self.deck)
        return self.new_card

    def get_points(self, user_input):
        """Comment"""
        diff = self.old_card - self.new_card
        if diff < 0 and user_input == True or diff > 0 and user_input == False:
            return 100
        return -75
    
    