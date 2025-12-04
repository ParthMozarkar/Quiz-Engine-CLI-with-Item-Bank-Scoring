Quiz Engine CLI + GUI with Item Bank & Scoring

A Python-based Quiz Engine that allows users to take quizzes via a
command-line interface (CLI) or

a modern Tkinter GUI, with dynamic question loading, Google Sheets
leaderboard integration, and

local fallback storage.

FEATURES

\- Dual Interface Support (CLI + GUI)

\- Dynamic Question Loading from JSON

\- Google Sheets Cloud Sync

\- Local CSV Fallback

\- Secure .env Configuration

\- Modular Architecture

TECH STACK

\- Python 3.12

\- Tkinter GUI

\- Google Sheets API + CSV backup

\- python-dotenv, gspread, oauth2client

SETUP INSTRUCTIONS

1\. Clone the repository

2\. Create virtual environment: python3 -m venv venv

3\. Activate it and install dependencies: pip install -r
requirements.txt

4\. Create .env file:

> GOOGLE_CREDS_PATH=credentials.json
>
> SPREADSHEET_ID=your_sheet_id_here

5\. Run main.py to start the GUI quiz

FILES & FOLDERS

main.py

ui.py

quiz_engine/

> \# Core controller

\# GUI interface

> \# Core modules (loader, evaluator, scorer)

data/Questions.json \# Question bank

data/leaderboard.csv \# Local leaderboard

.env, credentials.json \# Ignored for security

CLOUD & LOCAL STORAGE

\- Online mode: saves scores to Google Sheets

\- Offline mode: saves scores to local CSV

