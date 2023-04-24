import datetime
import json
import time

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required


# from birdbank.forms import UserLoginForm

# Create your views here.
from django.template import loader
from django.urls import reverse

from app.models import Account, Transaction


def index(request):
    return render(request, "index.html")


def login_view(request):
    context = {}
    context['message'] = ''
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/myaccounts')
        else:
            context['message'] = "Invalid User Credentials."
    return render(request, "login.html", context)
    '''
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/myaccounts')
    message=''
    try:
        message = form.errors.as_data()['__all__'][0].message
    except:
        pass
    context = {
        'form':form,
        'message':message
    }
    return render(request,"login.html",context)
    '''


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return HttpResponseRedirect(reverse('index'))


def myaccounts(request):
  myaccounts = Account.objects.all().values()
  template = loader.get_template('myaccounts.html')
  data = {}
  for myaccount in myaccounts:
    if myaccount['Type'] in data.keys():
        data[myaccount['Type']].append(myaccount)
    else:
        data[myaccount['Type']] = [myaccount]
  context = {
    'myaccounts': data,
  }
  return HttpResponse(template.render(context, request))


@login_required
def transactions(request):
    transactions = Transaction.objects.all().values()
    myaccounts = Account.objects.all().values()
    template = loader.get_template('transactions.html')
    data ={}
    for myaccount in myaccounts:
        if myaccount['Type'] in data.keys():
            data[myaccount['Type']].append(myaccount['AccountNumber'])
        else:
            data[myaccount['Type']] = [myaccount['AccountNumber']]
    context = {
        'transactions': transactions,
        'accounts': data
    }
    return HttpResponse(template.render(context, request))

@login_required
def transfer(request):
    myaccounts = Account.objects.all().values()
    template = loader.get_template('transfer.html')
    data = {}
    for myaccount in myaccounts:
        if myaccount['Type'] in data.keys():
            data[myaccount['Type']].append(myaccount)
        else:
            data[myaccount['Type']] = [myaccount]
    context = {
        'myaccounts': data,
    }
    return HttpResponse(template.render(context, request))

@login_required
def paybills(request):
    transactions = Transaction.objects.all().values()
    myaccounts = Account.objects.all().values()
    template = loader.get_template("paybills.html")
    data = {}
    for myaccount in myaccounts:
        if myaccount['Type'] in data.keys():
            data[myaccount['Type']].append(myaccount['AccountNumber'])
        else:
            data[myaccount['Type']] = [myaccount['AccountNumber']]
    context = {
        'transactions': transactions,
        'accounts': data
    }
    return HttpResponse(template.render(context, request))

@login_required
def purchase(request):
    return render(request, "purchase.html")

@login_required
def loans(request):
    return render(request, "loans.html")

@login_required
def help(request):
    return render(request, "help.html")

@login_required
def testreport(request):
    return render(request, "TestReport.html")

def forgotpassword(request):
    return render(request,"forgotpassword.html")


def getAccountNumber(request):
    if request.method == 'GET':
        type = request.GET['type']
        myaccounts = Account.objects.all().values()
        data = []
        for myaccount in myaccounts:
            if myaccount['Type'][:3] == type:
                data.append(myaccount['AccountNumber'])
        return HttpResponse(json.dumps({'data': data}), content_type="application/json")  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")


def getTransactions(request):
    if request.method == 'GET':
        accountNumber = request.GET['accountNumber']
        transactions = Transaction.objects.filter(AccountNumber = accountNumber).values()[:5]

        transactions = [{'Date':transaction['Date'].strftime("%m-%d-%Y"),'Type':transaction['Type'],'Particulars':transaction['Particulars'],'Amount':transaction['Amount'],'Balance':transaction['Balance']}for transaction in transactions]

        return HttpResponse(json.dumps({'transactions': transactions}), content_type="application/json")  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")