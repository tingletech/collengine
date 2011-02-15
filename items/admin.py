from .models import Item, DigitalFile
from django.contrib import admin
from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from django.contrib.admin.widgets import FilteredSelectMultiple
from vocabularies.models import Name

class DigitalFileInline(admin.TabularInline):
#class DigitalFileInline(admin.StackedInline):
    model = DigitalFile

class ItemForm(ModelForm):
    creatorWriter = forms.ModelMultipleChoiceField(queryset=Name.objects.all(), required=False, )
    class Meta:
        model = Item
    def save(self, commit=True):
        model = super(ItemForm, self).save(commit=False)
        ## turn querySet into List
        creatorWriterList = []
	for e in model.creatorWriter:
            creatorWriterList.append(e.id)
        model.creatorWriter = creatorWriterList

        if commit:
            model.save()
 
        return model


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
    form = ItemForm


admin.site.register(Item, ItemAdmin)
admin.site.register(DigitalFile)
