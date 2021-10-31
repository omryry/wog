from .memory_game import *
from .memory_game import play as play_memory
from .currency_roulette_game import *
from .currency_roulette_game import play as play_roulette
from .guess_game import *
from .guess_game import play as play_guess
from .score import *

def welcome(name):
    return "Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play"


def in_range(num1, num2, choice):
    if choice < num1 or choice > num2:
        return False
    else:
        return True


def load_game():
    won = False
    game = int(input('''
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS)
    '''))
    if not in_range(1, 3, game):
        print("Please choose a number between 1 and 3.")
        load_game()
    difficulty = int(input("Please choose game difficulty from 1 to 5: "))
    if not in_range(1, 5, difficulty):
        print("Please choose a number between 1 to 5.")
        load_game()
    if game == 1:
        won = play_memory(difficulty)
    elif game == 2:
        won = play_guess(difficulty)
    elif game == 3:
        won = play_roulette(difficulty)
    if won:
        add_score(difficulty)