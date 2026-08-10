from django.urls import path
from website.views import contact,index, about, newsletter_view
app_name = 'website'
urlpatterns = [
    path('', index,name= 'index' ),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('newsletter', newsletter_view, name='newsletter'),
]