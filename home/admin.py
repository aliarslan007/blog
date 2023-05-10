from django.contrib import admin
from .models import BlogModel


class BlogModelAdmin(admin.ModelAdmin):
    list_display=('image', 'title', 'content')


admin.site.register(BlogModel,BlogModelAdmin)
