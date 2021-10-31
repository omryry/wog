from currency_converter import CurrencyConverter
c = CurrencyConverter()
import random


def get_rate():
    rate = c.convert(100, 'USD', 'ILS')
    return rate / 100


def get_money_interval(rate, d, t):
    return t - (5 - d), t + (5 - d)


def get_guess_from_user():
    guess = int(input("What do you think is the amount in ILS? "))
    return guess


def play(difficulty):
    random_num = random.randint(1, 100)
    print(random_num)
    rate = get_rate()
    print(rate)
    ils_num = random_num * rate
    print(ils_num)
    interval = get_money_interval(rate, difficulty, random_num)
    print(interval)
    guess = get_guess_from_user()
    if guess < (ils_num - interval[0]) or guess > (ils_num + interval[1]):
        print(f"The number was {ils_num}")
        return False
    else:
        print(f"The number was {ils_num}")
        return True


if play(5):
    print("You Won!")
else:
    print("You Lose :(")
