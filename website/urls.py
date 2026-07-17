from django.urls import path
from website.views import contact,index, about

urlpatterns = [
    path('', index,name= 'index' ),
    path('contact', contact, name='contact'),
    path('about', about, name='about')
]