from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse('About me')
def contact(request):
    return HttpResponse('Contact me')
def tracker(request):
    return HttpResponse('Tracker me')
def search(request):
    return HttpResponse('Search me')
def prodectview(request):
    return HttpResponse('Prodict me')
def checkout(request):
    return HttpResponse('Checkout me')
