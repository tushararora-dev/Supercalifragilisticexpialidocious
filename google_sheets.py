# google_sheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet(sheet_name="StoryReviews"):
    """Authenticate and return the worksheet"""
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(creds)
    
    # Open spreadsheet (make sure this exists in your Google Drive)
    sheet = client.open(sheet_name).sheet1
    return sheet

def add_review(name, review, chapter_num):
    """Add a review row to Google Sheet"""
    sheet = get_sheet()
    sheet.append_row([name, review, chapter_num])

def get_all_reviews():
    """Fetch all reviews from Google Sheet"""
    sheet = get_sheet()
    return sheet.get_all_records()
