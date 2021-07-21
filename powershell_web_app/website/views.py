from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from NonPrimaryADAccounts.models import NonPrimaryADAccount

import subprocess
import json


def welcome(request):
    # userFirstName = subprocess.check_output([
    #     'powershell.exe',
    #     '[System.Security.Principal.WindowsIdentity]::GetCurrent().Name'
    # ])

    # response = ("Hello %s, welcome to my PowerShell Web App!") % userFirstName

    return render(request, "website/welcome.html",
                    {"secondary_account_count": NonPrimaryADAccount.objects.count()})


def date(request):
    return HttpResponse("This page was server at: " + str(datetime.now()))


def about(request):
    user = json.loads(subprocess.check_output([
        'powershell.exe',
        'Get-ADuser -Identity q1444317 -Properties SamAccountName| ConvertTo-Json'
    ]))

    response = ("Name: %s <br>"
                "LastName: %s <br>"
                "ID: %s") % (user["GivenName"], user["Surname"], user["SamAccountName"])

    return HttpResponse(response)