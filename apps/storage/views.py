from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    allproduct = product.objects.all()
    return render(request, 'index.html', {'allproduct':allproduct})

def contact(request):
    return render(request, 'contact.html')

def detalle(request):
    return render(request, 'detalle/menu.html')
