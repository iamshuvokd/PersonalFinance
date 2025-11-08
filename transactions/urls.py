from django.urls import path
from .views import  given, taken, transactions

urlpatterns = [
   path('', transactions),
   path('given/', given),
   path('taken/', taken),
]
