from django.contrib import admin

from manga.models import manga, Usuario

# Register your models here.

admin.site.register(manga)
admin.site.register(Usuario)