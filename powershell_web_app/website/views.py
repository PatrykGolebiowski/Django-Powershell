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
                    {"non_primary_ad_accounts": NonPrimaryADAccount.objects.all()})


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


def getaduser(request, id):
    get_ad_user = json.loads(subprocess.check_output([
        'powershell.exe',
        'Get-ADuser -Identity %s -Properties SamAccountName,Company,Department,EmailAddress,Title | ConvertTo-Json' % (id)
    ]))

    return render(request, "website/getaduser.html", {"ad_user": get_ad_user})