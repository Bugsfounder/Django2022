from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("This is contact Page")

def tracker(request):
    return HttpResponse("This is tracker Page")

def search(request):
    return HttpResponse("This is search Page")

def productview(request):
    return HttpResponse("This is productview Page")

def checkout(request):
    return HttpResponse("This is checkout Page")
