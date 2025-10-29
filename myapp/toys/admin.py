from django.contrib import admin
from .models import Category, Toy

admin.site.register(Toy)
admin.site.register(Category)