from .models import Item, DigitalFile
from django.contrib import admin
from django_tablib.admin import TablibAdmin
from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from django.contrib.admin.widgets import FilteredSelectMultiple
from vocabularies.models import Name, Place, Topic

class DigitalFileInline(admin.TabularInline):
#class DigitalFileInline(admin.StackedInline):
    model = DigitalFile

# http://www.hindsightlabs.com/blog/2010/02/11/adding-extra-fields-to-a-model-form-in-djangos-admin/
class ItemForm(ModelForm):
    creatorWriter = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('creatorWriter'), False), required=False, 
    )

    creatorDirector = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('creatorDirector'), False), required=False, 
    )

    creatorProducer = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('creatorProducer'), False), required=False, 
    )

    contributorEditor = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('contributorEditor'), False), required=False, 
    )

    contributorCamera = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('contributorCamera'), False), required=False, 
    )

    contributorSound = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('contributorSound'), False), required=False, 
    )

    contributorMusic = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('contributorMusic'), False), required=False, 
    )

    contributorCast = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('contributorCast'), False), required=False, 
    )

    contributorMusician = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('contributorMusician'), False), required=False, 
    )

    contributorPublisher = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('contributorPublisher'), False), required=False, 
    )

    contributorDistributor = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('contributorDistributor'), False), required=False, 
    )

    subjectName = forms.ModelMultipleChoiceField(
        queryset=Name.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('subjectName'), False), required=False, 
    )

    subjectPlace = forms.ModelMultipleChoiceField(
        queryset=Place.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('subjectPlace'), False), required=False, 
    )

    subjectTopic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(), widget = admin.widgets.FilteredSelectMultiple( ('subjectTopic'), False), required=False, 
    )


    class Meta:
        model = Item

    def save(self, commit=True):
        model = super(ItemForm, self).save(commit=False)
        ## turn querySet into List
        model.creatorWriter = [name.id for name in model.creatorWriter]
        model.creatorDirector = [name.id for name in model.creatorDirector]
        model.creatorProducer = [name.id for name in model.creatorProducer]
        model.contributorEditor = [name.id for name in model.contributorEditor]
        model.contributorCamera = [name.id for name in model.contributorCamera]
        model.contributorSound = [name.id for name in model.contributorSound]
        model.contributorMusic= [name.id for name in model.contributorMusic]
        model.contributorCast = [name.id for name in model.contributorCast]
        model.contributorMusician = [name.id for name in model.contributorMusician]
        model.contributorPublisher = [name.id for name in model.contributorPublisher]
        model.contributorDistributor = [name.id for name in model.contributorDistributor]
        model.subjectName = [name.id for name in model.subjectName]
        model.subjectPlace = [place.id for place in model.subjectPlace]
        model.subjectTopic = [topic.id for topic in model.subjectTopic]

        if commit:
            model.save()
 
        return model


#class ItemAdmin(admin.ModelAdmin):
class ItemAdmin(TablibAdmin):
    search_fields = [ 'title', 'projectId', 'localId', 'sourceId', 'barcode', 'aggregatorId', ]
    list_display = ( 'title', )
    list_filter = ( 'formatMediaType', )
    fieldsets = (
        ('Descriptive + Technical', {
            'fields': ('title', 'contributor', 'projectId', 'localId', 'sourceId', 'barcode', 'aggregatorId', 'creatorWriter', 'creatorDirector', 'creatorProducer', 'countryOfCreation', 'dateCreated', 'dateIssued', 'formatMediaType', 'physicalFormat', 'silent', 'formatColors', 'runningSpeed', 'totalReels', 'formatGeneration', 'formatDuration', ),
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
    formats = ['xls', 'json', 'yaml', 'csv', 'html',]

class DigitalFileAdmin(TablibAdmin):
    formats = ['xls', 'json', 'yaml', 'csv', 'html',]

admin.site.register(Item, ItemAdmin)
admin.site.register(DigitalFile, DigitalFileAdmin)
