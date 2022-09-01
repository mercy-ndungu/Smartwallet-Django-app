from django.urls import path
from .views import register_card, register_customer, register_notification, register_receipt, register_thirdparty, register_transaction
from .views import register_currency
from .views import register_wallet
from .views import register_account,register_loan,register_reward


urlpatterns =[ 
path("register/",register_customer,name="registration"),
path("registercurrency/",register_currency, name="registration"),
path("registerwallet/", register_wallet, name="registration"),
path("registeraccount/", register_account, name = "registration"),
path ("registertransaction/", register_transaction, name = "registration"),
path ("registercard/", register_card,name="registration"),
path ("registerthirdparty/", register_thirdparty, name="registration"),
path ("registernotification/", register_notification, name="registration"),
path ("registerreceipt/", register_receipt, name="registration"),
path ("registerloan/", register_loan, name="registration"),
path ("registerreward/", register_reward, name="registration"),
]