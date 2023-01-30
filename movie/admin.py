from django.contrib import admin

from movie.models import Movie

# Register your models here.
admin.site.register(Movie)

# @admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','infor','publish',  'desc')
    # prepopulated_fields = {'slug':('title',) }
