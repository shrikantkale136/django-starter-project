from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'demo/home.html')

def about(request):
     return render(request, 'demo/about.html')
