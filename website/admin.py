from django.contrib import admin
from website.models import Contact
# Register your models here.

#@admin.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    #fields = ["name",]
    list_display = [ "name", "email","subject"]
#admin.site.register(Post)
    list_filter = ['email']
    #ordering = ['created_date']
    search_fields = ['name', 'message','subject']