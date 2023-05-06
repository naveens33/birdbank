"""birdbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login_view, name='login_view'),
    path('logout',views.logout_view,name='logout_view'),
    path('myaccounts', views.myaccounts, name='myaccounts'),
    path('transactions', views.transactions, name='transactions'),
    path('transfer', views.transfer, name='transfer'),
    path('paybills', views.paybills, name='paybills'),
    path('purchase', views.purchase, name='purchase'),
    path('loans', views.loans, name='loans'),
    path('help', views.help, name='help'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('testreport', views.testreport, name='testreport'),
    url(r'^getAccountNumbers/$', views.getAccountNumber, name='getAccountNumbers'),
    url(r'^getTransactions/$', views.getTransactions, name='getTransactions')
]
