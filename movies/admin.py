from django.contrib import admin
from movies.models import *


class MovieAdmin(admin.ModelAdmin):
    fields = ['title']


admin.site.register(Movie)
admin.site.register(Review)

