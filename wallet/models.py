from ast import mod
from curses.ascii import NUL
from distutils.command.upload import upload
from email.policy import default
from inspect import signature
from locale import currency
from pyexpat import model
# from tkinter import CASCADE
from termios import TAB1
from time import timezone
# from tkinter import CASCADE
from unittest import mock
from django.db import models
# from requests import delete

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15,null=True)
    last_name = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=10,null=True)
    address = models.TextField()
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=15,null=True)
    id_number = models.CharField(max_length=10,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    email = models.EmailField()
    proile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    marital_status=models.CharField(max_length=8,null=True)
    employment_status = models.BooleanField(null=True)
    signature=models.ImageField(default='default.jpg',upload_to='profile_pics')



class Wallet(models.Model):
    balance = models.IntegerField(default="")
    customer_id = models.IntegerField(default="")
    # currency=models.ForeignKey(on_delete=CASCADE,null=True)
    time = models.DateTimeField(default="")
    status = models.CharField(max_length=15,default="")
    history = models.DateTimeField(default="")
    pin = models.CharField(max_length=15,default="")
    active=models.BooleanField(null=True)
    datecreated=models.DateTimeField(default="")
    type=models.CharField(max_length=8,null=True)


class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=30)
    balance = models.IntegerField()
    saving=models.IntegerField
    name = models.CharField(max_length=30)
    wallet = models.ForeignKey(Wallet, on_delete= models.CASCADE)

class Transaction(models.Model):
    transaction_code = models.CharField(max_length=30)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    transaction_amount = models.IntegerField()
    transaction_type = models.CharField(max_length=30)
    transaction_charge = models.IntegerField()
    transaction_time = models.DateTimeField()
    reciept = models.CharField(max_length=8,null=True)
    # origin_account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True)
    destination_account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True)

class Card(models.Model):
    issue_date = models.CharField(max_length=30)
    card_name = models.CharField(max_length=30)
    card_number = models.IntegerField()
    card_type = models.CharField(max_length=30)
    expiry_date = models.DateTimeField()
    card_status = models.CharField(max_length=30)
    security_code = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    issuer = models.CharField(max_length=30)

class Third_Party(models.Model):
    name = models.CharField(max_length=15)
    id = models.CharField(max_length=8)
    type = models.CharField(max_length=6)
    transaction_account = models.IntegerField()
    account = models.OneToOneField(Account,on_delete=models.CASCADE,primary_key=True)
    currency = models.CharField(max_length=3)

class Notifications(models.Model):
    transaction = models.CharField(max_length=15)
    transaction_id = models.IntegerField()
    transaction_amount = models.BigIntegerField()
    customer_id = models.IntegerField()
    status = models.CharField(max_length=6)
    transaction_number =models.CharField(max_length=7)
    date_time = models.DateTimeField()
    recipient = models.OneToOneField
    transaction_description = models.CharField(max_length=10)

class Receipt(models.Model):
    receipt_type = models.CharField(max_length=15)
    receipt_date = models.DateTimeField()
    bill_number = models.IntegerField()
    total_amount = models.IntegerField()
    # transaction = models.ForeignKey()
    receipt_file = models.FileField()

class Loan(models.Model):
    loan_id = models.BigIntegerField()
    loan_type = models.CharField(max_length=15)
    amount = models.BigIntegerField()
    datetime = models.DateTimeField()
    Wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    intrest_rate = models.IntegerField()
    payment_due_date = models.DateTimeField()
    loan_balance = models.IntegerField()
    guaranter = models.ForeignKey(Third_Party,on_delete=models.CASCADE,null=True) 


class Reward(models.Model):
    name = models.CharField(max_length=15)
    customer_id = models.IntegerField()
    gender = models.CharField(max_length=6)
    points = models.IntegerField()
    date_of_reward = models.DateTimeField()
    recipient = models.OneToOneField(Account,on_delete=models.CASCADE,null=True)