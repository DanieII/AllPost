from django.contrib import admin

from posts.models import Post, Tag, Comments

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)