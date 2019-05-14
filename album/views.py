from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

# Create your views here.
def home(request):
    images=Image.display_images()
    return render(request, 'all-images/welcome.html', {"images":images})

def sports_category(request):
    return render(request, 'all-images/sports.html')
