from django.contrib import admin

# Register your models here.
from .models import Category, Car, Color


class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price', 'image')


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Car, CarAdmin)
