from django.contrib import admin
from blog.models import Tag, Post, PostAdmin

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

