from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def sports_category(request):
    return render(request, 'all-images/sports.html')
