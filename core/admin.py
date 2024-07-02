
from django.contrib import admin

from .models import Day, Hotel, blog, gallery, package
admin.site.register(package)
admin.site.register(blog)
admin.site.register(Day)
admin.site.register(Hotel)
admin.site.register(gallery)