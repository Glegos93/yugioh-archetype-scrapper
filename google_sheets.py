import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheets_data(spreadsheet_name, sheet_name, range_name):
    # Define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Add your service account credentials file
    creds = ServiceAccountCredentials.from_json_keyfile_name('yugioh-archetype.json', scope)

    # Authorize the client sheet 
    client = gspread.authorize(creds)

    # Get the instance of the Spreadsheet
    sheet = client.open(spreadsheet_name).worksheet(sheet_name)

    # Get the data from the specified range
    data = sheet.get(range_name)
    
    return data