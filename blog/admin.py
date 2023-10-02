from django.contrib import admin
from blog.models import Tag, Post, PostAdmin, Comment

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)