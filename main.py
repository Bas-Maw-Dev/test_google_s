import os
import pygsheets
from dotenv import load_dotenv

# Get gsheets data from KEYS file
load_dotenv()
PATH_TO_G_SHEETS_KEY = os.getenv("PATH_TO_G_SHEETS_KEY")

# Create the Client
client = pygsheets.authorize(service_account_file=PATH_TO_G_SHEETS_KEY)

# opens a spreadsheet by its name/title
spreadsht = client.open('PygSheets_Test2411071402')

# opens a worksheet by its name/title
worksht = spreadsht.worksheet("title", "Sheet1")

worksht.cell("A1").set_text_format("bold", True).value = "Lots of stuff"

worksht.update_values("A2:A6", [["Pencils"], ["Eraser"],
                                ["Sharpeners"], ["Ruler"],
                                ["Pens"]])

worksht.update_values("B2:B6", [["10"], ["10"],
                                ["10"], ["10"],
                                ["10"]])