class Card:
    def __init__(self, identity, location):
        self.identity = identity
        self.location = location
        self.intersect = False

    def __str__(self):
        return self.location

    def __eq__(self, other):
        return self.location == other.location


if __name__ == '__main__':
    card1 = Card('Player1', 'A1')
    card2 = Card('       ', 'B1')
    card3 = Card('Monster', 'D4')
