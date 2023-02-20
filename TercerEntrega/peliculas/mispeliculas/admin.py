from django.contrib import admin
from .models import Pelicula, Series, Capitulo
# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Series)
admin.site.register(Capitulo)