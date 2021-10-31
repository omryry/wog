import os
scores_file_name = "scores.txt"
bad_return_code = 1
files_path = "/Users/oweiss/PycharmProjects/DevOps0507/WoG"

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')