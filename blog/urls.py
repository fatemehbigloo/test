from django.urls import path
from blog.views import blog_single,blog_views
app_name = 'blog'
urlpatterns = [
    path('', blog_views, name = 'home' ),
    path('single', blog_single, name='single')
]