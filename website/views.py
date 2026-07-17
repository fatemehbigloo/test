from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(requstes):
    return render(requstes,'website/index.html')