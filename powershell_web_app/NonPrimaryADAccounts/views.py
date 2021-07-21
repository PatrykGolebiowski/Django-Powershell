from django.shortcuts import render, get_object_or_404, redirect
from .models import NonPrimaryADAccount
from django.forms import modelform_factory
import subprocess

def detail(request, id):
    non_primary_ad_account = get_object_or_404(NonPrimaryADAccount, pk=id)
    return render(request, "NonPrimaryADAccounts/detail.html", {"non_primary_ad_account": non_primary_ad_account})


NonPrimaryADAccountForm = modelform_factory(NonPrimaryADAccount, exclude=['PrimaryID'])

def newaduser(request):
    if (request.method == "POST"):
        # form has been submitted, process data
        form = NonPrimaryADAccountForm(request.POST)
        if (form.is_valid()):
            form.save()
            subprocess.run([
                'powershell.exe',
                """$credentials = Get-Credential

                    New-AdUser `
                    -Name '%s' `
                    -SamAccountName '%s'`
                    -UserPrincipalName '%s@qvcdev.qvc.net'`
                    -GivenName '%s'`
                    -Surname '%s'`
                    -Description '%s'`
                    -EmailAddress '%s'`
                    -Title '%s'`
                    -Department '%s'`
                    -Company '%s'`
                    -Path 'OU=Users,OU=IT,OU=Poland,DC=qvcdev,DC=qvc,DC=net' `
                    -Credential $credentials""" % (request.POST['SecondaryID'], request.POST['SecondaryID'], request.POST['SecondaryID'], request.POST['FirstName'], 
                                                    request.POST['Surname'], "Created via Django", request.POST['EmailAddress'],
                                                    request.POST['JobTitle'], request.POST['Department'], request.POST['Company'])
            ])
            return redirect("welcome")
    else:
        form = NonPrimaryADAccountForm()
    return render(request, "NonPrimaryADAccounts/NewADuser.html", {"form": form})