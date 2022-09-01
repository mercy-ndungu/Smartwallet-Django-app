# from pyexpat import model
from django import forms
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
         model= Customer
         fields = "__all__"
   

    # How to create form in django to collect data for the entities.
    # A mete class provides data of the clss your are inheriting from
class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
         model= Currency
         fields = "__all__"

class WalletRegistrationForm(forms.ModelForm):
     class Meta:
          model= Wallet
          fields = "__all__"

class AccountRegistrationForm(forms.ModelForm):
     class Meta:
          model= Account
          fields = "__all__"

class TransactionRegistrationForm(forms.ModelForm):
     class Meta:
          model = Transaction
          fields = "__all__"

class CardRegistrationForm(forms.ModelForm):
     class Meta:
          model=Card
          fields = "__all__"

class ThirdpartyRegistrationForm(forms.ModelForm):
     class Meta:
          model = ThirdParty
          fields = "__all__"

class NotificationRegistrationForm(forms.ModelForm):
     class Meta:
          model = Notification
          fields= "__all__"

class ReceiptRegistrationForm(forms.ModelForm):
     class Meta:
          model = Receipt
          fields = "__all__"

class LoanRegistrationForm(forms.ModelForm):
     class Meta:
          model= Loan
          fields = "__all__"

class RewardRegistrationForm(forms.ModelForm):
     class Meta:
          model= Reward
          fields= "__all__"