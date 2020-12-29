from django.contrib import admin

from new_app.models import Author, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
