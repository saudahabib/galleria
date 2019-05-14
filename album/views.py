from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

# Create your views here.
def home(request):
    images=Image.display_images()
    return render(request, 'all-images/welcome.html', {"images":images})

def sports_category(request):
    return render(request, 'all-images/sports.html')

def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term=request.GET.get("category")
        searched_images=Image.search_by_cat(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message, "images": searched_images})
    else:
        message="Type in a category to search"
        return render(request, 'all-images/search.html',{"message":message})
