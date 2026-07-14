from django.shortcuts import render
from django.http import HttpResponse

def home(requstes):
    return HttpResponse("<h1> home </h1>")