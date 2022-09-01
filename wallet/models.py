
from django.utils import timezone
from django.db import models



class Customer(models.Model):
    first_name=models.CharField(max_length=20, null=True)
    last_name=models.CharField(max_length=20, null=True)
    address=models.TextField()
    # password = models.CharField(max_length=8) 
    email=models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=13, null=True)
    gender=models.CharField(max_length=10, null=True)
    age=models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length=20, null=True)
    # employment=models.BooleanField()
    profile_picture = models.ImageField(default='default.jpg',upload_to='profile pics')

class Currency(models.Model):
    country= models.CharField(max_length=54)
    symbol= models.CharField(max_length=12)
    amount= models.BigIntegerField()

class Wallet(models.Model):
    balance = models.IntegerField(null=True)
    customer = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name='Wallet_customer',null=True)
    amount  = models.IntegerField(null=True)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=15, null=True)
    currency = models.ForeignKey("Currency",on_delete=models.CASCADE,related_name='Wallet_currency', null=True)
    history = models.DateTimeField(default=timezone.now)
    pin = models.IntegerField(null=True)

class Account(models.Model):
    account_name = models.CharField(max_length=30, null=True)
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=7)
    account_balance = models.IntegerField(null=True)
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Account_wallet')

class Transaction(models.Model):
    message = models.CharField(max_length=600,null=True)
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Transaction_wallet',null=True)
    transaction_description = models.CharField(max_length=270, null=True)
    transaction_amount = models.IntegerField(null=True)
    transaction_type = models.CharField(max_length=30, null=True)
    origin_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_origin',null=True)
    destination_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_destination',null=True)

class Card(models.Model):
    card_number= models.IntegerField()
    card_type= models.CharField(max_length=20)
    expiry_date = models.DateTimeField(default=timezone.now)
    security_code = models.IntegerField()
    date_of_issue = models.DateTimeField(default=timezone.now)
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Card_wallet',null=True)
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Card_account',null=True)
    issuer= models.CharField(max_length=10)

class ThirdParty(models.Model):
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Thirdparty_account')
    transaction_amount= models.BigIntegerField()
    currency = models.ForeignKey("Currency",on_delete=models.CASCADE,related_name='Thirdparty_currency')
    date_of_issue = models.DateTimeField(default=timezone.now)
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Thirdparty_wallet')
    issuer= models.CharField(max_length=20)

class Notification(models.Model):
    message= models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    recipient= models.ForeignKey("Customer",on_delete=models.CASCADE,related_name='Thirdparty_recipient')
    title = models.CharField(max_length=20) 

class Receipt(models.Model):
    receipt_type= models.CharField(max_length = 23, null=True)
    date = models.DateTimeField(default=timezone.now)
    receipt_number= models.IntegerField()
    amount= models.IntegerField()
    transaction = models.ForeignKey("Transaction",on_delete=models.CASCADE,related_name='Thirdparty_transaction',null=True)
    receipt_file = models.FileField()

class Loan(models.Model):
    loan_id = models.IntegerField()
    loan_type = models.CharField(max_length=15)
    loan_balance = models.IntegerField()
    amount = models.IntegerField()
    guaranter = models.CharField(max_length=20, null=True)
    issuer = models.CharField(max_length=20, null=True)
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Loan_wallet',null=True)

class Reward(models.Model):
    transaction= models.ForeignKey("Transaction",on_delete=models.CASCADE,related_name='Reward_transaction',null=True)
    recipient = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name='Reward_recipient',null=True)
    date_of_reward = models.DateTimeField(default=timezone.now)
    points = models.IntegerField()                                        

