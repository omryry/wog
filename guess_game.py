import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    user_guess = 0
    while user_guess < 1 or user_guess > difficulty:
        user_guess = input("Please choose a number between 1 and " + str(difficulty) + ": ")
    return user_guess


def compare_results(random_num, user_guess):
    if random_num == user_guess:
        return True
    else:
        return False


def play(difficulty):
    num1 = generate_number(difficulty)
    num2 = get_guess_from_user(difficulty)
    if compare_results(num1, num2):
        print("You Won :)")
        print("The number was " + str(num1))
        return True
    else:
        print("You Lost :(")
        print("The number was " + str(num1))
        return False
