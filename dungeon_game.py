from dungeon_cards import Card
import random


class Game:

    def __init__(self):
        self.size = 5
        self.card_options = ['Player1', 'Monster', 'Escape ', '       ',
                             '       ', '       ', '       ', '       ',
                             '       ', '       ', '       ', '       ',
                             '       ', '       ', '       ', '       ',
                             '       ', '       ', '       ', '       ',
                             '       ', '       ', '       ', '       ', '       ']
        self.columns = ['A', 'B', 'C', 'D', 'E']
        self.cards = []
        self.locations = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                self.locations.append(f'{column}{num}')

    # define the 'cards' (arrangement of player1, monster, and escape exit) in the grid
    def set_cards(self):
        used_locations = []  # make a list for the used locations
        # for each option in card_options
        for option in self.card_options:
            # make an object for available locations
            available_locations = set(self.locations) - set(used_locations)
            # choose a random location from that list
            chosen_location = random.choice(list(available_locations))
            # make a card with the chosen card option and location
            card = Card(option, chosen_location)
            # add the card to the list of cards
            self.cards.append(card)
            # append used location to used location
            used_locations.append(chosen_location)

    # create rows
    def create_row(self, num):
        row = []
        while True:
            for column in self.columns:
                for card in self.cards:
                    if card.location == f'{column}{num}':
                        if not card.intersect:
                            if card.identity == 'Player1':
                                row.append(card.identity)
                            else:
                                row.append('       ')
                        else:
                            row.append(card.identity)  # if any of the player cards intersect the row will show them
            return row

    # create the grid
    def create_grid(self):
        # | A | B | C | D | this what it looks like
        header = '  |    ' + '    |    '.join(
            self.columns) + '    |'  # create a header that has the column names and borders on the outside
        print(header)  # print out the header
        #        print('   ---------------------------------------')
        for row in range(1, self.size + 1):
            # print a row header
            print_row = f'{row} | '
            # create an object for the row (use create_row)
            get_row = self.create_row(row)
            # print the row with borders
            print_row += ' | '.join(get_row) + ' |'
            print(print_row)

    def check_player1_location(self):
        for card in self.cards:
            if card.identity == "Player1":
                return card

    def check_monster_location(self):
        for card in self.cards:
            if card.identity == "Monster":
                return card

    def check_move(self):
        while True:
            move = input(f'Where would you like to move?  ')
            if move.upper() in self.locations:
                if move.upper() == str(self.check_player1_location()):
                    print("You're already there! Please make a new move.")
                else:

                    if (abs(ord([*move.upper()][0]) - ord([*str(self.check_player1_location())][0])) <= 1) and (
                            abs(int([*move.upper()][1]) - int(
                                    [*str(self.check_player1_location())][1])) <= 1):  # [*] separates 'A' from '1'
                        if (abs(ord([*move.upper()][0]) - ord([*str(self.check_monster_location())][0])) <= 1) and (
                                abs(int([*move.upper()][1]) - int([*str(self.check_monster_location())][1])) <= 1):
                            print(
                                "########################################## WATCH OUT!!!! The monster's gaining on you!"
                                "#####################################")
                        return move.upper()
                    else:
                        print("That is not a valid move. You may only move one space.")
            else:
                print("That is not a valid move. It should look like this: A1")

    def switch_positions(self, card1, card2):
        card1_location = card1.location
        card2_location = card2.location  # create objects for the locations
        card1.location = card2_location
        card2.location = card1_location  # switch the locations
        return card1, card2

    def move_player1(self, loc1):
        list_of_locations = []
        for card in self.cards:
            if card.location == loc1:
                list_of_locations.append(card)  # add the player input move to the list first
        list_of_locations.append(self.check_player1_location())  # add player 1 location to list
        if list_of_locations[0].identity == '       ':
            self.switch_positions(list_of_locations[0], list_of_locations[1])  # need to define "switch_positions"
            return True
        else:
            list_of_locations[0].intersect = True
            list_of_locations[1].intersect = True
            self.create_grid()
            if list_of_locations[0].identity == 'Monster':
                print('The monster found you. May God have mercy on your soul.')
            else:
                print('Yayyyyyyy you escaped!')

            return False

    def end_game(self):
        for card in self.cards:
            if card.intersect:
                return True
            else:
                return False

    def start_game(self):
        game_running = True
        print(
            "This is the dungeon game. To move your player on the board, "
            "submit the grid location of where you would like to go. If you find the Escape Door, you win. "
            "If the monster finds you first, you lose.")
        self.set_cards()
        while game_running:
            self.create_grid()
            move1 = self.check_move()
            if not self.move_player1(move1):
                if self.end_game():
                    game_running = False


if __name__ == '__main__':
    game = Game()
    game.start_game()
