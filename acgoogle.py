import appJar
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the Google Sheets credentials
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDS_FILE = ("credentials.json")

# Create a new Google Sheet
def create_new_sheet():
    # Load the Google Sheets credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = gspread.authorize(credentials)

    # Prompt the user to enter the new sheet name
    sheet_name = appJar.textBox("New Sheet Name", "Enter a name for the new sheet:")

    # Create the new sheet
    try:
        sheet = client.create(sheet_name)
        appJar.infoBox("Success", f"New sheet '{sheet_name}' created!")
    except Exception as e:
        appJar.errorBox("Error", str(e))

# Create the GUI
app = appJar.gui("Create a New Google Sheet")

# Add a button to create a new sheet
app.addButton("Create New Sheet", create_new_sheet)

# Start the GUI
app.go()
