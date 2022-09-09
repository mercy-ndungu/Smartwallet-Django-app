from django.urls import path
from . import views
from .views import register_card, register_customer, register_notification, register_receipt, register_thirdparty, register_transaction
from .views import register_currency
from .views import register_wallet
from .views import register_account,register_loan,register_reward


urlpatterns =[ 
path("register/",register_customer,name="registration"),
path("registercurrency/",register_currency, name="registration"),
path("registerwallet/", register_wallet, name="registration"),
path("registeraccount/", register_account, name = "registration"),
path("registertransaction/", register_transaction, name = "registration"),
path("registercard/", register_card,name="registration"),
path("registerthirdparty/", register_thirdparty, name="registration"),
path("registernotification/", register_notification, name="registration"),
path("registerreceipt/", register_receipt, name="registration"),
path("registerloan/", register_loan, name="registration"),
path("registerreward/", register_reward, name="registration"),
path("customer/",views.list_customers, name="list_customers"),
path("currencies/",views.list_currency, name="list_currency"),
path("wallets/",views.list_wallet, name="list_wallet"),
path("accounts/",views.list_account, name="list_account"),
path("transactions/",views.list_transactions, name="list_transactions"),
path("transactions/",views.list_transactions, name="list_transactions"),


]