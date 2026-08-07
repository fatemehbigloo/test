# blog/views.py
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def blog_views(request, **kwargs):
    posts = Post.objects.filter(status=1)  # cat رو اختیاری کن
    if kwargs.get('cat') != None:  # اگه cat توی آدرس بود
        posts = Post.objects.filter(status=True, category__name=kwargs['cat'])
    if kwargs.get('username') != None:
        posts = Post.objects.filter(status=True, author__username=kwargs['username'])

    posts = Paginator(posts, 2)
    try :  
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger :
        posts = posts.get_page(1)
    except EmptyPage :
        posts = posts.get_page(1)
    context = {'posts': posts,}
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

def blog_search(request):
    posts = Post.objects.filter(status=1)  # cat رو اختیاری کن
    
    if request.method == 'GET':
        posts = posts.filter(content__contains = request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    context = {'posts': posts,}
    return render(request, 'blog/blog_views.html', context)
