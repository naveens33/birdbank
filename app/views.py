from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required


# from birdbank.forms import UserLoginForm

# Create your views here.
from django.urls import reverse



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


@login_required
def myaccounts(request):
    return render(request, "myaccounts.html")

@login_required
def transactions(request):
    return render(request, "transactions.html")

@login_required
def transfer(request):
    return render(request, "transfer.html")

@login_required
def paybills(request):
    return render(request, "paybills.html")

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