from django.shortcuts import render, redirect  
from website.forms import NameForm, ContantForm , NewsLetterForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect  
from website.models import Contact
from django.views.decorators.csrf import csrf_protect


def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContantForm (request.POST)
        if form.is_valid():
            form.cleaned_data['name']
            form.save()
        else :
            return HttpResponse('Not Valid')
    form = ContantForm()
    return render(request,'website/contact.html', {'form':form})


@csrf_protect
def newsletter_view(request):
    if request.method == 'POST' :
        form = NewsLetterForm (request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else :
        return HttpResponseRedirect('/')