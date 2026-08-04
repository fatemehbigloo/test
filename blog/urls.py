from django.urls import path
from blog.views import blog_single,blog_views,blog_category
app_name = 'blog'
urlpatterns = [
    path('', blog_views, name = 'home' ),
    path('<int:pid>/', blog_single, name='single'),
    path('category/<str:cat>/', blog_views, name='category'),
]