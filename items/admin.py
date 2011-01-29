from .models import Item, DigitalFile
from django.contrib import admin

class DigitalFileInline(admin.TabularInline):
#class DigitalFileInline(admin.StackedInline):
    model = DigitalFile

class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descriptive + Technical', {
            'fields': ('title', 'contributor', 'projectId', 'localId', 'aggregatorId', 'creatorWriter', 'creatorDirector', 'creatorProducer', 'countryOfCreation', 'dateCreated', 'dateIssued', 'formatMediaType', 'physicalFormat', 'silent', 'formatColors', 'runningSpeed', 'totalReels', 'formatGeneration', 'formatDuration', 'fileNameUniquePart',),
            'description': 'description blah blah'
        }),
        ('Additional Descriptive', {
            'classes': ('collapse',),
            'fields': ( 'alternativeTitle', 'seriesTitle', 'contributorCamera', 'contributorEditor', 'contributorSound', 'contributorMusic','contributorCast', 'contributorMusician', 'contributorPublisher','contributorDistributor', 'collection', 'descriptionGeneralNote','descriptionAbstract', 'descriptionContents', 'descriptionTranscript','descriptionShotList', 'language', 'subjectName', 'subjectPlace', 'subjectTopic', 'genreForm')
        }),
        ('Additional Technical', {
            'classes': ('collapse',),
            'fields': ('stockManufacturer', 'formatStandard', 'carrierFormat', 'carrierId', 'carrierPartNumber', 'carrierAdditionalPhysicalDescription', 'carrierCondition', 'carrierAssessedDate')
        }),
    )
    inlines = [
        DigitalFileInline,
    ]


admin.site.register(Item, ItemAdmin)
admin.site.register(DigitalFile)
