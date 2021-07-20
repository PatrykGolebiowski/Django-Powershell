from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import subprocess
# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the Powershell Web App!")


def date(request):
    return HttpResponse("This page was server at: " + str(datetime.now()))


def about(request):
    response = subprocess.check_output([
        'powershell.exe',
        'Get-Process | ft'
    ])
    return HttpResponse(response)