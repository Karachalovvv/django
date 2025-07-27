from django.contrib import admin
from posts.models import Post, Category, Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ["title", "content", "rate", "category"]
#     search_fields = ["title", "content"]
#     list_editable = ["rate"]