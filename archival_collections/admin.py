from .models import Collection
from django.contrib import admin
from django_tablib.admin import TablibAdmin

class CollectionAdmin(TablibAdmin):
    formats = ['xls', 'json', 'yaml', 'csv', 'html',]

admin.site.register(Collection, CollectionAdmin)
