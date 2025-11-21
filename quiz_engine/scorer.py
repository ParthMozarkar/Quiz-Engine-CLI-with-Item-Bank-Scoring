import csv
from datetime import datetime

def calculate_score(correct, total):
    return round((correct / total) * 100, 2)

def save_score(username, correct, total, path="data/Leaderboard.csv"):
    percentage = calculate_score(correct, total)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, correct, total, percentage, timestamp])

    print("Score saved to Leaderboard.csv")
