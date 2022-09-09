


from locale import currency
from django.shortcuts import render
from wallet.models import Currency, Notification, ThirdParty, Wallet
from .forms import CustomerRegistrationForm, RewardRegistrationForm, WalletRegistrationForm,CardRegistrationForm,ThirdpartyRegistrationForm,ReceiptRegistrationForm
from .forms import CurrencyRegistrationForm, AccountRegistrationForm,TransactionRegistrationForm,NotificationRegistrationForm
from .forms import LoanRegistrationForm
from.models import Customer
# The puporse of this view.py is to handle https
# A http request is composed by a request and a response fromthe cloud.
# This  is where the customer enters and saves data .
# Accepts only one argument(request)
# Create your views here.
# Then get our route via url.py

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form = CustomerRegistrationForm()
    return render (request,"wallet/register_customer.html",{"form":form})
def list_customers(request):
    customer =Customer.objects.all()
    return render (request,"wallet/list_customers.html",{"customer":customer})



def register_currency(request):
    if request.method == 'POST':
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form = CurrencyRegistrationForm()
    return render (request,"wallet/register_currency.html",{"form":form})
def list_currency(request):
    currencies = Currency.objects.all()
    return render (request,"wallet/list_currency.html",{"currency":currency})



def register_wallet(request):
    if request.method == 'POST':
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form = WalletRegistrationForm()
    return render (request,"wallet/register_wallet.html",{"form":form})
def list_wallet(request):
    wallets = Wallet.objects.all()
    return render (request,"wallet/list_wallet.html",{"wallet":wallets})






def register_account(request):
    if request.method == 'POST':
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form = AccountRegistrationForm()
    return render (request,"wallet/register_account.html",{"form":form})
def list_account(request):
    accounts = AccountRegistrationForm()
    return render (request, "wallet/list_account.html", {"accounts":accounts})






def register_transaction(request):
    if request.method == 'POST':
        form =TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form = TransactionRegistrationForm()
    return render (request,"wallet/register_transaction.html",{"form":form})
def list_transactions(request):    
    transactions = TransactionRegistrationForm()
    return render (request, "wallet/list_transaction.html", {"transactions":transactions})








    

def register_card(request):
    if request.method == 'POST':
        form =CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form = CardRegistrationForm()
    return render (request,"wallet/register_card.html",{"form":form})
def list_card(request):
    cards = CardRegistrationForm()
    return render (request, "wallet/list_card.html", {"cards":cards})








def register_thirdparty(request):
    if request.method == 'POST':
        form =ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form = ThirdpartyRegistrationForm()
    return render (request,"wallet/register_thirdparty.html",{"form":form})
def list_thirdparty(request):
    cards = ThirdpartyRegistrationForm()
    return render (request,"wallet/list_thirdparty.html", {"card":cards})






def register_notification(request):
    if request.method == 'POST':
        form =NotificationRegistrationForm(request.POST)
    if form.is_valid():
            form.save()
    else:
       form = NotificationRegistrationForm()
    return render (request,"wallet/register_notification.html",{"form":form})
def list_notification(request):
    notifications = NotificationRegistrationForm()
    return render (request, "wallet/list_notification.html", {"notifications":notifications})





def register_receipt(request):
    if request.method == 'POST':
        form =ReceiptRegistrationForm(request.POST)
    if form.is_valid():
            form.save()
    else:
       form = ReceiptRegistrationForm()
    return render (request,"wallet/register_reciept.html",{"form":form})
def list_reciept(request):
    receipts = ReceiptRegistrationForm()
    return render (request, "wallet/list_receipt.html", {"reciept":receipts})







def register_loan(request):
    if request.method == 'POST':
        form =LoanRegistrationForm(request.POST)
    if form.is_valid():
            form.save()
    else:
       form = LoanRegistrationForm()
    return render (request,"wallet/register_loan.html",{"form":form})
def list_loan(request):
    loans = LoanRegistrationForm()
    return render(request, "wallet/list_loan.html",{"loans":loans})





def register_reward(request):
    if request.method == 'POST':
        form =RewardRegistrationForm(request.POST)
    if form.is_valid():
            form.save()
    else:
       form =RewardRegistrationForm()
    return render (request,"wallet/register_reward.html",{"form":form})
def list_reward(request):
    rewards = RewardRegistrationForm()
    return render (request, "wallet/list_reward.html", {"form":rewards})