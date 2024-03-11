from django.contrib import admin
from blog.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]


admin.site.register(Post, PostModelAdmin)
# Register your models here.
