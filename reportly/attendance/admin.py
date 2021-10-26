from django.contrib import admin
from .models import Book,Students
# Register your models here.
# admin.site.register(Book)
# admin.site.register(Students)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title','no_of_pages','isbn','date']
    list_editable=['isbn']
    search_fields=['title','body']

