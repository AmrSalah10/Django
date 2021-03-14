from django.contrib import admin
from .models import Movie, Category
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','year')
    list_filter = ["year",'categories']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)