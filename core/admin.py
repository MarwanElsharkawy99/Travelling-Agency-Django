from django.contrib import admin

from .models import blog, package
admin.site.register(package)
admin.site.register(blog)