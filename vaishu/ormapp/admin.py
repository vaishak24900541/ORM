from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'director', 'release_date', 'rating')
    list_filter = ('genre', 'release_date', 'rating')
    search_fields = ('title', 'director', 'genre')
    ordering = ('-release_date',)

