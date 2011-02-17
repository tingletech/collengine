from .models import Name, Place, Topic
from django.contrib import admin
from django_tablib.admin import TablibAdmin

class NameAdmin(TablibAdmin):
    formats = ['xls', 'json', 'yaml', 'csv', 'html',]

class PlaceAdmin(TablibAdmin):
    formats = ['xls', 'json', 'yaml', 'csv', 'html',]

class TopicAdmin(TablibAdmin):
    formats = ['xls', 'json', 'yaml', 'csv', 'html',]

admin.site.register(Name, NameAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Topic, TopicAdmin)

