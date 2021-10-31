from .utils import *
import os


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    if not (os.path.exists(os.path.join(files_path, scores_file_name))):
        with open(os.path.join(files_path, scores_file_name), "w+") as scores_file:
            scores_file.write("0")
    with open(os.path.join(files_path, scores_file_name), "a+") as scores_file:
        scores_file.seek(0)
        sum_score = scores_file.read()
        sum_score = int(sum_score)
        sum_score = sum_score + points_of_winning
        scores_file.seek(0)
        scores_file.truncate()
        scores_file.write(str(sum_score))