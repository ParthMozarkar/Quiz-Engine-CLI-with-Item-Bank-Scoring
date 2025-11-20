import json
import random

def load_questions(path):
    with open(path, "r") as f:
        data = json.load(f)

    random.shuffle(data)
    return data

