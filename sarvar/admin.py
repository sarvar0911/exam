from django.contrib import admin
from sarvar.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    search_fields = ["title", ]
    list_filter = ["author", ]
