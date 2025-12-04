import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_key('1ZtYOPnloR2QaMW8MEU-rKrlS4s-EMkEk6oMYtiPBYn8').sheet1
sheet.append_row(["Anirudh", "10", "10", "100%", "2025-12-04 21:00"])
print("✅ Successfully connected and wrote to Google Sheets!")
