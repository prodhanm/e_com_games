from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')
# Create your views here.
def cart(request):
    return render(request, 'cart.html')
