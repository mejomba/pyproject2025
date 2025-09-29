from django.contrib import admin

from core.models import Category, Tag

admin.site.register([Category, Tag])
