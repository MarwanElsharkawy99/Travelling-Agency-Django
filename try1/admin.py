from django.contrib import admin
from .models import Package, Day, Activity

class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 1

class DayInline(admin.TabularInline):
    model = Day
    extra = 1

class PackageAdmin(admin.ModelAdmin):
    inlines = [DayInline]

class DayAdmin(admin.ModelAdmin):
    inlines = [ActivityInline]

admin.site.register(Package, PackageAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Activity)
