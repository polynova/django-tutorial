from django.contrib import admin

#Register your models here.

from catalog.models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)

#Define the admin class

# Define the admin class
# class AuthorAdmin(admin.ModelAdmin):
#     pass

# Register the admin class with the associated model
# admin.site.register(Author) 


admin.site.register(Genre)
# admin.site.register(BookInstance)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')



