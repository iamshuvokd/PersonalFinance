from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def transactions(request):
   return HttpResponse('Welcome to Transactions Page')

def given(request):
   return HttpResponse('Welcome to Given Page')

def taken(request):
   return HttpResponse('Welcome to Taken Page')