from django import template
from blog.models import Post 
from blog.models import Category
register = template.Library()

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts


@register.filter()
def snipper(value,arg=20):
    return value[:arg]+ "..."


@register.inclusion_tag('blog/blog_papulerpost.html')
def papuler_post():
    posts = Post.objects.filter(status=1).order_by('published_date')[:2]
    return {'posts':posts}




@register.inclusion_tag('blog/blog_categories.html')  # تغییر مسیر به فایل موجود
def categories():
    categories = Category.objects.all()
    # ایجاد لیستی از آبجکت‌های Category با تعداد پست‌ها
    category_list = []
    for cat in categories:
        count = Post.objects.filter(status=1, category=cat).count()
        category_list.append({
            'category': cat,
            'count': count
        })
    return {'category_list': category_list}


