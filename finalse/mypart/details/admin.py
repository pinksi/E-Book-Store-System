from django.contrib import admin
from .models import Book
from .models import Category
from django.apps import AppConfig

class BookAdmin(admin.ModelAdmin):
	list_display= ["__str__", "author","price", "date_added", "pub_date", "clicks", "category"]
	
class CategoryAdmin(admin.ModelAdmin):
	list_display= ["__str__"]
	
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)


# Register your models here.
