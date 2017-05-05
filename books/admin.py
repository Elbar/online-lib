from django.contrib import admin
from django.contrib.admin import AdminSite
from models import Book

# Register your models here.
AdminSite.site_header = "Online Library"

admin.site.register(Book)
