from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Привет")
def home(request):
    return render(request, 'index.html')
def top_sellers(request):
    return render(request, 'top-sellers.html')