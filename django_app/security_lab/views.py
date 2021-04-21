from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

#import library
import gspread
#Service client credential from oauth2client
from oauth2client.service_account import ServiceAccountCredentials
# Print nicely
import pprint
#Create scope

DIRNAME = os.path.dirname(__file__)

def security_lab(request):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]
    #create some credential using that scope and content of startup_funding.json
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(DIRNAME, 'ASRG- Security-Lab-3ccc4fb856c3.json'),scope)
    #create gspread authorize using that credential
    client = gspread.authorize(creds)
    #Now will can access our google sheets we call client.open on StartupName
    sheet = client.open('Copy of Automotive Security Lab').sheet1
    pp = pprint.PrettyPrinter()
    #Access all of the record inside that
    result = sheet.get_all_values()
    # pp.pprint(result)
    result = list(result)
    return HttpResponse(len(result))
