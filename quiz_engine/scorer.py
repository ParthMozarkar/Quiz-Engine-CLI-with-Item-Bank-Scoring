import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import csv
import os

class CloudScorer:
    def __init__(self):
        # ⭐ REPLACE THIS WITH YOUR SPREADSHEET ID
        self.SPREADSHEET_ID = "1wQmJBhAUMYkra6Z1OlPGETmbmU4x1aOOe5O3i0nn7Z8"
        
        self.sheet = None
        self.connected = False
        
        # Fallback to local CSV if cloud fails
        self.local_csv = "data/leaderboard.csv"
        
        self.connect_to_cloud()
    
    def connect_to_cloud(self):
        """Connect to Google Sheets"""
        try:
            print("🔄 Connecting to Cloud Leaderboard...")
            
            # Define the scope
            scope = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
            
            # Add credentials from JSON file
            creds = ServiceAccountCredentials.from_json_keyfile_name(
                'credentials.json', 
                scope
            )
            
            # Authorize and connect
            client = gspread.authorize(creds)
            
            # Open the spreadsheet by ID
            spreadsheet = client.open_by_key(self.SPREADSHEET_ID)
            self.sheet = spreadsheet.sheet1  # Get first sheet
            
            self.connected = True
            print("✅ Connected to Cloud Leaderboard!")
            
        except FileNotFoundError:
            print("⚠️  credentials.json not found in project folder.")
            print("    Using local CSV backup instead.")
            self.connected = False
        except gspread.exceptions.APIError as e:
            print(f"⚠️  Google Sheets API Error: {e}")
            print("    Using local CSV backup instead.")
            self.connected = False
        except Exception as e:
            print(f"⚠️  Cloud connection failed: {e}")
            print("    Using local CSV backup instead.")
            self.connected = False
    
    def save_score(self, username, score, total):
        """Save score to cloud or local CSV"""
        percentage = (score / total) * 100 if total > 0 else 0
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Try cloud first
        if self.connected and self.sheet:
            try:
                print(f"💾 Saving {username}'s score to cloud...")
                
                self.sheet.append_row([
                    username,
                    score,
                    total,
                    f"{percentage:.1f}%",
                    timestamp
                ])
                
                print(f"✅ Score saved to cloud for {username}!")
                return True
                
            except Exception as e:
                print(f"⚠️  Cloud save failed: {e}")
                print("    Saving to local CSV instead...")
        
        # Fallback to local CSV
        self.save_to_local_csv(username, score, total, percentage, timestamp)
        return True
    
    def save_to_local_csv(self, username, score, total, percentage, timestamp):
        """Fallback: Save to local CSV file"""
        os.makedirs("data", exist_ok=True)
        
        file_exists = os.path.exists(self.local_csv)
        
        with open(self.local_csv, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header if new file
            if not file_exists:
                writer.writerow(['Name', 'Score', 'Total', 'Percentage', 'Date'])
            
            writer.writerow([username, score, total, f"{percentage:.1f}%", timestamp])
        
        print(f"✅ Score saved locally for {username}")
    
    def get_leaderboard(self, top_n=10):
        """Get top scores from cloud or local"""
        if self.connected and self.sheet:
            try:
                print("📊 Loading leaderboard from cloud...")
                
                # Get all records from cloud
                records = self.sheet.get_all_records()
                
                if not records:
                    print("📭 No scores yet in the leaderboard!")
                    return []
                
                # Sort by score (descending), then by percentage
                sorted_records = sorted(
                    records, 
                    key=lambda x: (
                        int(x.get('Score', 0)), 
                        float(str(x.get('Percentage', '0%')).rstrip('%'))
                    ),
                    reverse=True
                )
                
                print(f"✅ Loaded {len(sorted_records)} scores from cloud!")
                return sorted_records[:top_n]
                
            except Exception as e:
                print(f"⚠️  Failed to get cloud leaderboard: {e}")
                print("    Loading from local CSV instead...")
        
        # Fallback to local CSV
        return self.get_local_leaderboard(top_n)
    
    def get_local_leaderboard(self, top_n=10):
        """Get leaderboard from local CSV"""
        if not os.path.exists(self.local_csv):
            print("📭 No local leaderboard file found.")
            return []
        
        try:
            with open(self.local_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                records = list(reader)
            
            if not records:
                return []
            
            # Sort by score
            sorted_records = sorted(
                records,
                key=lambda x: (
                    int(x.get('Score', 0)),
                    float(str(x.get('Percentage', '0%')).rstrip('%'))
                ),
                reverse=True
            )
            
            print(f"✅ Loaded {len(sorted_records)} scores from local CSV")
            return sorted_records[:top_n]
            
        except Exception as e:
            print(f"⚠️  Error reading local leaderboard: {e}")
            return []


def calculate_score(correct, total):
    """Calculate percentage score"""
    if total == 0:
        return 0
    return (correct / total) * 100


# Initialize global scorer
print("\n" + "="*50)
print("🎮 Quiz Engine Pro - Initializing...")
print("="*50)
scorer = CloudScorer()
print("="*50 + "\n")


def save_score(username, score, total):
    """Public function to save score"""
    scorer.save_score(username, score, total)


def get_leaderboard(top_n=10):
    """Public function to get leaderboard"""
    return scorer.get_leaderboard(top_n)