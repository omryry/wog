import random
from time import sleep
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_sequence(difficulty):
    list = []
    for i in range(1, difficulty):
        num = random.randint(1, 101)
        list.append(num)
    list.sort()
    return list


def get_list_from_user(difficulty):
    list = []
    for i in range(1, difficulty):
        try:
            num = int(input("Please choose a number you remember: "))
        except ValueError:
            print("Please enter a number")
        list.append(num)
    list.sort()
    return list


def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False


def play(difficulty):
    won = False
    difficulty += 1
    list1 = generate_sequence(difficulty)
    print(list1)
    sleep(0.7)
    clear()
    list2 = get_list_from_user(difficulty)
    if is_list_equal(list1, list2):
        print("You Won!")
        won = True
    else:
        print("You Lost :(")
    print(f"The numbers were  {list1}")
    return won


play(5)
