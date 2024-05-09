from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request, 'index.html')

def paris_view(request):
    # Your view logic here
    return render(request, 'paris.html')

def gallery_view(request):
    # Your view logic goes here
    return render(request, 'index.html')

def dubai_view(request):
    # Your view logic here
    return render(request, 'dubai.html')

def singapore_view(request):
    # Your view logic here
    return render(request, 'singapore.html')

def italy_view(request):
    # Your view logic here
    return render(request, 'italy.html')

def contact_view(request):
    # Your view logic here
    return render(request, 'contact.html')

def thailand_view(request):
    # Your view logic here
    return render(request, 'thailand.html')

def maldives_view(request):
    # Your view logic here
    return render(request, 'maldives.html')

def switzerland_view(request):
    # Your view logic here
    return render(request, 'switzerland.html')

def egypt_view(request):
    # Your view logic here
    return render(request, 'egypt.html')

def book_view(request):
    # Your view logic here
    return render(request, 'book.html')

def germany_view(request):
    # Your view logic here
    return render(request, 'germany.html')

def aust_view(request):
    # Your view logic here
    return render(request, 'aust.html')