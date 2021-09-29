"""
Welcome to my trial version of BlackJack.
This version is meant to contain:
    - an AI dealer;
    - a human player;
    - a regular deck of cards; and
    - a bank roll.
I am ignoring actions like:
    - insurance;
    - splitting on a pair; and
    - doubling down.
I am hoping to come back to this at some point and address the pieces being ignored. Mainly for the practice and
challenge.
At this time I am unsure of how to handle Aces. I have them counting as 11 right now but need to work in the value of 1
if the player goes over 21. Working on that now.
"""

import random
import time
import os

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


#############################################################################

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


##############################################################################

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    # With the deck created we now need to shuffle it.
    def shuffle(self):
        random.shuffle(self.all_cards)

    # Dealing cards so that they are removed from the Deck using pop()
    def deal_one(self):
        return self.all_cards.pop()


################################################################################

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # For a list of multiple cards
            self.all_cards.extend(new_cards)
        else:
            # For a single card
            self.all_cards.append(new_cards)

    @staticmethod
    def hand_set():
        for card_object in game_player.all_cards:
            numbers = int(card_object.value)
            player_hand_total.append(numbers)
        print(
            f"First card: {game_player.all_cards[0]}\nSecond Card: {game_player.all_cards[1]}\n{game_player.name}, you have:",
            sum(player_hand_total))

    @staticmethod
    def player_choice():
        choice = ''
        while choice not in ["Hit", "Stand"]:
            choice = input("Please choose Hit or Stand.\n")
            if choice not in ["Hit", "Stand"]:
                print("Sorry, invalid option!")

            elif choice == "Hit":
                game_player.add_cards(new_deck.deal_one())
                player_hand_total.append(int(game_player.all_cards[-1].value))
                print(f"You received: {game_player.all_cards[-1]}\nYou now have:", sum(player_hand_total))
                if sum(player_hand_total) == 21:
                    print("21!")
                elif sum(player_hand_total) < 21:
                    choice = ''
                else:
                    print("BUST!")
                    win_loss.append("Loss")

            else:
                print(f"You chose to {choice} at {sum(player_hand_total)}")
                break

        return choice

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


#################################################################################

class Dealer:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # For a list of multiple cards
            self.all_cards.extend(new_cards)
        else:
            # For a single card
            self.all_cards.append(new_cards)

    @staticmethod
    def hand_set():
        for card_object in game_dealer.all_cards:
            numbers = int(card_object.value)
            dealer_hand_total.append(numbers)
        print(
            f"The {game_dealer.name} is showing: {game_dealer.all_cards[0]}")

    @staticmethod
    def dealer_choice():
        choice = ''
        while choice not in ["Hit", "Stand"]:
            # if sum(player_hand_total) <= sum(dealer_hand_total):
            #     choice = "Stand"
            #     win_loss.append("Loss")
            #     print(f"House wins with {sum(dealer_hand_total)}")
            if sum(player_hand_total) > sum(dealer_hand_total):
                choice = "Hit"
                game_dealer.add_cards(new_deck.deal_one())
                dealer_hand_total.append(int(game_dealer.all_cards[-1].value))
                print(f"The {game_dealer.name} Hit and now has ", sum(dealer_hand_total))
                if sum(dealer_hand_total) > 21:
                    win_loss.append("Win")
                    print(f"{game_dealer.name} BUSTS!")
                elif sum(dealer_hand_total) == 21:
                    win_loss.append("Loss")
                    print("House wins with 21!")
                elif sum(dealer_hand_total) == sum(player_hand_total):
                    win_loss.append("Loss")
                    print("House Wins!")
                elif sum(dealer_hand_total) > sum(player_hand_total):
                    win_loss.append("Loss")
                    print("House Wins!")
                elif sum(player_hand_total) > sum(dealer_hand_total):
                    choice = ''
                else:
                    pass
            elif sum(player_hand_total) <= sum(dealer_hand_total):
                choice = "Stand"
                win_loss.append("Loss")
                print(f"House wins with {sum(dealer_hand_total)}")
            else:
                break

    def __str__(self):
        return f"Player {game_dealer.name} has {len(self.all_cards)} cards."


#################################################################################

class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{game_player.name} your starting bank roll is ${self.balance}. If you hit $0 or double your money the game ends.'

    def player_win(self):
        if "Win" in win_loss and sum(player_hand_total) != 21:
            self.balance = self.balance + 5
            print(f"You're current bank roll is ${self.balance}")
        elif "Win" in win_loss and sum(player_hand_total) == 21:
            self.balance = self.balance + 10
        elif "Loss" in win_loss:
            self.balance = self.balance - 5
            print(f"You're current bank roll is ${self.balance}")


###################################################################################

# Letting players choose to keep playing or not.
def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input("Keep playing? (Y or N) ")

        if choice not in ['Y', 'N']:
            print("Sorry, please choose Y or N ")

    if choice == 'Y':
        return True

    else:
        return False


####################################################################################

# Game Setup
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to BlackJack. \nDesigned by Donny Neely")
game_player = Player(input("Please let me know what to call you!\n"))
game_dealer = Dealer("AI Dealer")
bank_roll = Bank(game_player.name, 50)
print(bank_roll)
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')
new_deck = Deck()
new_deck.shuffle()
player_hand_total = []
dealer_hand_total = []
win_loss = []
game_on = True
while game_on:
    while 1 < bank_roll.balance < 100:
        game_player.all_cards.clear()
        game_dealer.all_cards.clear()
        player_hand_total.clear()
        dealer_hand_total.clear()
        win_loss.clear()

        for x in range(2):
            game_dealer.add_cards(new_deck.deal_one())

        Dealer.hand_set()

        for x in range(2):
            game_player.add_cards(new_deck.deal_one())

        Player.hand_set()
        Player.player_choice()
        bank_roll.player_win()

        if sum(player_hand_total) <= 21:
            Dealer.dealer_choice()
            bank_roll.player_win()

        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        break

print("Awe you're out of money! Thanks for playing!'")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
