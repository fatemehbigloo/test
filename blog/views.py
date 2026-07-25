from django.shortcuts import render
from blog.models import Post
# Create your views here.
from django.http import HttpResponse
def blog_views(request):
    posts = Post.objects.filter(status=1)
    context = {'posts' :posts}
    return render(request,'blog/blog_views.html', context)

def blog_single(request, pid):
    print("\n--- DEBUG START ---")
    print(f"Target PID: {pid}")

    try:
        # مرحله اول: تلاش برای گرفتن پست بدون هیچ شرط اضافه‌ای
        post = Post.objects.get(pk=pid)
        
        print(f"SUCCESS: Post found!")
        print(f"DEBUG: Title: {post.title}")
        print(f"DEBUG: Status: {post.status}")
        print(f"DEBUG: Content: {post.content[:20]}...") # فقط ۲۰ کاراکتر اول برای تست
        
        return render(request, 'blog/blog_single.html', {'post': post})

    except Post.DoesNotExist:
        print(f"ERROR: Post")