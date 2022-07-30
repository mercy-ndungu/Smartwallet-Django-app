from django.contrib import admin
from .models import Account, Customer, Transaction
from .models import Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name")
admin.site.register(Customer, CustomerAdmin)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ("account_number ","account_type", "balance","name", "wallet")
#     search_fields = ("account_number", "account_type")
# admin.site.register(Account, AccountAdmin)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)



