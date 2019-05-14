from django.contrib import admin
from .models import Image, Location, Category
# Register your models here.
'''
Registering models in admin
'''


admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
