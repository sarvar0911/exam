from django.contrib import admin
from sarvar.models import Post, Profile, About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
