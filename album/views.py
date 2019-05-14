from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def sports_category(request):
    return HttpResponse('This is the sports category')
