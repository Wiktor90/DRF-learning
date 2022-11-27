from django.contrib import admin
from blog.models import Author, Post, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "email", "nick")
    # list_filter = ('status', 'due_back')
    #
    # fieldsets = (
    #     (None, {
    #         'fields': ('book', 'imprint', 'id')
    #     }),
    #     ('Availability', {
    #         'fields': ('status', 'due_back')
    #     }),
    # )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "text", "created_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "text")
