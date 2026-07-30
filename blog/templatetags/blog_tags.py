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




@register.inclusion_tag('blog/blog_catgories.html')
def catgories():
    posts = Post.objects.filter(status=1).order_by('category')
    all_categories = Category.objects.all()
    cta_dict = {}
    #count of category
    for cat in all_categories:
        count = Post.objects.filter(status=1, category=cat).count()
        cta_dict[cat] = count
    return {"catgories": cta_dict}