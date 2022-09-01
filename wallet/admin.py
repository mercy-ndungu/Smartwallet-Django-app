from django.contrib import admin
from .models import Customer,Account,Transaction,Notification,Receipt,Reward
from.models import Currency
from .models import Wallet
from.models import ThirdParty
from .models import Card
from .models import Loan

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email',)
    search_fields = ('first_name','last_name',)
admin.site.register(Customer,CustomerAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('amount','symbol',)
    search_fields = ('amount',)
admin.site.register(Currency,CurrencyAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('Customer','balance','date_created',)
    search_fields = ('Customer',)
admin.site.register(Wallet)

class AccountAdAdmin(admin.ModelAdmin):
    list_display = ('account_name','account_number','account_type',)
    search_fields = ('account_name','account_number','account_type',)
admin.site.register(Account,AccountAdAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet','message','transaction_description','transaction_type','destination_account',)
    search_fields = ('transaction_description','transaction_type',)
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_type','card_number','date_of_issue','expiry_date','wallet','issuer','account',)
    search_fields = ('card_type','card_number','issuer',)
admin.site.register(Card,CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ('account','transaction_amount','currency','date_of_issue','wallet',)
    search_fields = ('date_of_issue',)
admin.site.register(ThirdParty,ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title','message','date','recipient')
    search_fields = ('title','message','date','recipient')
admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_type','date','receipt_number','receipt_file',)
    search_fields = ('receipt_type','date','receipt_file')
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id','loan_type','loan_balance','guaranter','amount','issuer','wallet',)
    search_fields = ('guaranter','issuer','loan_id',)
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('transaction',)
    search_fields = ('transaction',)
admin.site.register(Reward)


