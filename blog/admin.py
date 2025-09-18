from django.contrib import admin
from blog.models import post


@admin.register(post.Post)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "created_at", "publish_at")

    def get_queryset(self, request):
        return post.Post.objects.all()

