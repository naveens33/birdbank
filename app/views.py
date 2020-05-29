from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def myaccounts(request):
    return render(request,"myaccounts.html")


def transactions(request):
    return render(request,"transactions.html")

def transfer(request):
    return render(request,"transfer.html")

def testreport(request):
    return render(request,"TestReport.html")