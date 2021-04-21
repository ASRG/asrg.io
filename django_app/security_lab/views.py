from django.shortcuts import render
from django.http import HttpResponse
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

DIRNAME = os.path.dirname(__file__)
# Create your views here.


def security_lab(request):
    context = {}
    data = []
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(DIRNAME, 'ASRG- Security-Lab-3ccc4fb856c3.json'),scope)
    client = gspread.authorize(creds)
    sheet = client.open('Copy of Automotive Security Lab').sheet1
    pp = pprint.PrettyPrinter()
    result = sheet.get_all_values()
    result = list(result)
    context['theading'] = list(result[8])
    for i in  range(9,len(result)):
        data.append(list(result[i]))
    context['data'] = data
    # return HttpResponse(len(result))
    return render(request, "security_lab.html", context)
