from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

admin.site.register(Genre)
admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    filter_horizontal = ('genre',)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    # Fieldsets group fields into visual sections on the edit page
    fieldsets = (
        ('Book Details', {
            'fields': ('book', 'id')
        }),
        ('Availability Status', {
            'fields': ('status', 'due_back')
        }),
    )