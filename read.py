from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials

SERVICE_ACCOUNT_FILE = "C://Users//benja//Escritorio//scrapsy//gold_coins_spider//keys.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '14cxO8m9DfZq4Y9PYuVqoSXJQmHD0L5p3y-XJc5-DUUI'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="P.OBJETIVO!I3:I32").execute()
values = result.get('values', [])
# values.pop(2)
# values.pop(2)
# values.pop(6)
flatList = [element for innerList in values for element in innerList]
commas_list = [s.replace('.', ',') for s in flatList]
new_list = [int(s.replace(',', '')) for s in commas_list]


class Read():
    def read_american_normal(self):
        american_eagle_normal_shipping = []
        american_eagle_normal_shipping.extend([new_list[29], new_list[25], new_list[28], new_list[22]])
        return american_eagle_normal_shipping

    def read_american_express(self):
        american_eagle_express_shipping = []
        american_eagle_express_shipping.extend([new_list[24], new_list[27], new_list[23], new_list[26]])
        return american_eagle_express_shipping

    def read_canadian(self):
        canadian_maple = []
        canadian_maple.extend([new_list[10], new_list[9], new_list[7], new_list[6]])
        return canadian_maple


read = Read()
print(read.read_american_normal())
print(read.read_american_express())
print(read.read_canadian())