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

def menu(request):
    return render(request, 'menu.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')
    
def test(request):
    return render(request, 'test.html')

def logout(request):
    return render(request, 'logout.html')

