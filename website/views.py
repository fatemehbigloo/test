from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(requstes):
    return render(requstes,'website/index.html')

def about(requstes):
    return render(requstes,'website/about.html')

def contact(requstes):
    return render(requstes,'website/contact.html')