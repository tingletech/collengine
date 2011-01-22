from .models import Item, DigitalFile
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descriptive + Technical', {
            'fields': ('title', 'contributor', 'projectId', 'localId', 'aggregatorId', 'creatorWriter', 'creatorDirector', 'creatorProducer', 'countryOfCreation', 'dateCreated', 'dateIssued', 'formatMediaType', 'formatPhysicalY', 'silent', 'formatColors', 'runningSpeed', 'totalReels', 'formatGeneration', 'formatDuration', 'fileNameUniquePart',)
        }),
        ('Additional Descriptive', {
            'classes': ('collapse',),
            'fields': ( 'alternativeTitle', 'seriesTitle', 'contributorCamera', 'contributorEditor', 'contributorSound', 'contributorMusic','contributorCast', 'contributorMusician', 'contributorPublisher','contributorDistributor', 'collection', 'descriptionGeneralNote','descriptionAbstract', 'descriptionContents', 'descriptionTranscript','descriptionShotList', 'language', 'subjectName', 'subjectPlace', 'subjectTopic', 'genreForm')
        }),
        ('Additional Technical', {
            'classes': ('collapse',),
            'fields': ('formatPhysicalX', 'formatStandard', 'carrierFormat', 'carrierId', 'carrierPartNumber', 'carrierAdditionalPhysicalDescription', 'carrierCondition', 'carrierAssessedDate')
        }),
    )

admin.site.register(Item, ItemAdmin)
admin.site.register(DigitalFile)
