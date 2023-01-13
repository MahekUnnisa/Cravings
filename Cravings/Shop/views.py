from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def recepies(request):
    return render(request, 'recepies.html')

def contact(request):
    return render(request, 'contact.html')

def test(request):
    return render(request, 'test.html')