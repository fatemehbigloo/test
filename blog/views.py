from django.shortcuts import render
from blog.models import Post
# Create your views here.
from django.http import HttpResponse
def blog_views(request):
    posts = Post.objects.filter(status=1)
    context = {'posts' :posts}
    return render(request,'blog/blog_views.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    context = {'posts' :posts}
    return render(request, 'blog/blog_single.html',context)