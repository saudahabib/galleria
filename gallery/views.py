from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    '''
    View to welcome user on home page
    '''
    return HttpResponse("Welcoome to Galleria")
