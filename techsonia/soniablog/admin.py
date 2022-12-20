

from django.contrib import admin
from .models import Post, Comment
from .models import  SubscribedUsers
from . models import CustomUser


# Customize the way the admin panel looks
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')  # displays the properties mentioned in the tuple
    list_filter = ('created_on',) 
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')




# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(SubscribedUsers, SubscribedUsersAdmin)

admin.site.register(CustomUser)
