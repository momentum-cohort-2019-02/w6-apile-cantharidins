from django.contrib import admin
from core.models import Post, Vote, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Comment)

