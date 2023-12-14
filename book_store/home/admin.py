from django.contrib import admin
from . models import category, books, library
# Register your models here.


class catadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(category, catadmin)

class bookadmin(admin.ModelAdmin):
    list_display = ['name','stock','price','available', 'img']
    list_editable = ['stock','price','available', 'img']
    prepopulated_fields={'slug':('name',)}
admin.site.register(books, bookadmin)

class libradmin(admin.ModelAdmin):
    list_display = ['name','img','available', 'file']
    list_editable = ['img','file','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(library, libradmin)

