from django.contrib import admin
from blog.models import Post,Category
# Register your models here.
admin.site.register(Category)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    #fields = ["name",]
    list_display = [ "title","author", "published_date","content", "status", "counted_views"]
#admin.site.register(Post)
    list_filter = ['status', "author"]
    #ordering = ['created_date']
    search_fields = ['content', 'title']



