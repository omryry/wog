from .utils import *
import os
from flask import Flask, render_template

def score_server():
    try:
        scores_file = open(os.path.join(files_path, scores_file_name), "r")
        scores_file.seek(0)
        score = scores_file.read()
        return render_template("scores_html.html", SCORE=score)
    except:
        return render_template("error_html.html", ERROR="There was an error")