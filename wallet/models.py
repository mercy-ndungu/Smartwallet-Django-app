from pyexpat import model
from unicodedata import name
from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=15)
    id_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    proile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    employment_status = models.BooleanField()


class Wallet(models.Model):
    balance = models.IntegerField(default="")
    customer_id = models.IntegerField(default="")
    time = models.DateTimeField(default="")
    status = models.CharField(max_length=15,default="")
    history = models.DateTimeField(default="")
    pin = models.CharField(max_length=15,default="")


class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=30)
    balance = models.IntegerField()
    name = models.CharField(max_length=30)
    wallet = models.ForeignKey(Wallet, on_delete= models.CASCADE)

class Transaction(models.Model):
    transaction_code = models.CharField(max_length=30)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    transaction_amount = models.IntegerField()
    transaction_type = models.CharField(max_length=30)
    transaction_charge = models.IntegerField()
    transaction_time = models.DateTimeField()
    # reciept = models.ForeignKey(Reciept, on_delete=models.CASCADE)
    # origin_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # destination_account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Card(models.Models):
    issue_date = models.CharField(max_length=30)
    card_name = models.CharField(max_length=30)
    card_number = models.IntegerField()
    card_type = models.CharField(max_length=30)
    expiry_date = models.DateTimeField(default=" ")
    card_status = models.CharField(max_length=30)
    security_code = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    issuer = models.CharField(max_length=30)

class Third_Party(models.model):
    name = models.CharField()
    id = models.CharField()
    type = models.CharField()
    transaction_account = models.IntegerField()
    account = models.ForeignKey()
    currency = models.CharField()

class Notifications(models.model):
    transaction = models.CharField()
    transaction_id = models.BigAutoField()
    transaction_amount = models.BigAutoField()
    Customer_id = models.BigAutoField()
    status = models.CharField()
    transaction_number =models.CharField()
    date_time = models.DateTimeField()
    recipient = models.OneToOneField
    transaction_description = models.CharField()

class Receipt(models.model):
    receipt_type = models.CharField()
    receipt_date = models.DateTimeField()
    bill_number = models.BigAutoField()
    total_amount = models.IntegerField()
    transaction = models.ForeignKey()
    receipt_file = models.FieldFile()

class Loan(models.model):
    loan_id = models.BigIntegerField()
    loan_type = models.CharField()
    amount = models.BigIntegerField()
    datetime = models.DateTimeField()
    Wallet = models.ForeignKey()
    intrest_rate = models.IntegerField()
    payment_due_date = models.DateTimeField()
    loan_balance = models.IntegerField()
    guaranter = models.ForeignKey() 


class Reward(models.model):
    name = models.CharField()
    customer_id = models.BigAutoField()
    gender = models.CharField()
    points = models.IntegerField()
    date_of_reward = models.DateTimeField()
    recipient = models.OneToOneField()


    
