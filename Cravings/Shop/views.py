from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def recepies(request):
    return render(request, 'recepies.html')
