from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def blog_views(requstes):
    return render(requstes,'blog/blog_views.html')

def blog_single(requstes):
    return render(requstes,'blog/blog_single.html')