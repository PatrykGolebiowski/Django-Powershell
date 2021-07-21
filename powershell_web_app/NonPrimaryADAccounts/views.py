from django.shortcuts import render, get_object_or_404
from .models import NonPrimaryADAccount

def detail(request, id):
    non_primary_ad_account = get_object_or_404(NonPrimaryADAccount, pk=id)
    return render(request, "NonPrimaryADAccounts/detail.html", {"non_primary_ad_account": non_primary_ad_account})