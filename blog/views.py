# blog/views.py
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category

def blog_views(request, cat=None):
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()  # اضافه کنید
    
    if cat:
        posts = Post.objects.filter(category__name=cat)
    
    context = {
        'posts': posts,
        'categories': categories,  # اضافه کنید
    }
    return render(request, 'blog/blog_views.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    categories = Category.objects.all()  # اضافه کنید
    
    return render(request, 'blog/blog_single.html', {
        'post': post,
        'categories': categories,  # اضافه کنید
    })

def blog_category(request, cat):
    category_obj = get_object_or_404(Category, name=cat)
    posts = Post.objects.filter(category__name=category_obj, status=1)
    categories = Category.objects.all()  # اضافه کنید
    
    context = {
        'posts': posts,
        'category': category_obj,
        'categories': categories,  # اضافه کنید
    }
    return render(request, 'blog/blog_views.html', context)