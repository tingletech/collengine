from djangotoolbox.fields import ListField, SetField, DictField, EmbeddedModelField
from institutions.models import Institution
from archival_collections.models import Collection
from vocabularies.models import Name, Place, Topic
from django.db import models
from django.contrib import admin

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=200)
    contributor = models.ForeignKey(Institution)
    projectId = models.CharField(max_length=200)
    localId = models.CharField(max_length=200)
    aggregatorId = models.CharField(max_length=200)
    creatorWriter = models.ForeignKey(Name, related_name="writer", null=True, blank=True)
    creatorDirector = models.ForeignKey(Name, related_name="director", null=True, blank=True)
    creatorProducer = models.ForeignKey(Name, related_name="producer", null=True, blank=True)
    countryOfCreation = models.CharField(max_length=2)
    dateCreated = models.DateField()
    dateIssued = models.DateField(null=True, blank=True)
    formatMediaType = models.CharField(max_length=200)
    formatPhysicalY = models.CharField(max_length=200)
    silent = models.CharField(max_length=200)
    formatColors = models.CharField(max_length=200)
    runningSpeed = models.CharField(max_length=200)
    totalReels = models.IntegerField()
    formatGeneration = models.CharField(max_length=200)
    formatDuration = models.CharField(max_length=200)
    fileNameUniquePart = models.CharField(max_length=200)

    alternativeTitle = models.CharField(max_length=200, blank=True)
    seriesTitle = models.CharField(max_length=200, blank=True)
    contributorEditor = models.CharField(max_length=200, blank=True)
    contributorCamera = models.CharField(max_length=200, blank=True)
    contributorSound = models.CharField(max_length=200, blank=True)
    contributorMusic = models.CharField(max_length=200, blank=True)
    contributorCast = models.CharField(max_length=200, blank=True) 
    contributorMusician = models.CharField(max_length=200, blank=True)
    contributorPublisher = models.CharField(max_length=200, blank=True)
    contributorDistributor = models.CharField(max_length=200, blank=True)
    collection = models.ForeignKey(Collection, null=True, blank=True)
    descriptionGeneralNote = models.TextField(blank=True)
    descriptionAbstract = models.TextField(blank=True)
    descriptionContents = models.TextField(blank=True)
    descriptionTranscript = models.TextField(blank=True)
    descriptionShotList = models.TextField(blank=True)
    language = models.CharField(max_length=2, blank=True)
    subjectName = models.ForeignKey(Name, related_name="subject_name", null=True, blank=True)
    subjectPlace = models.ForeignKey(Place, null=True, blank=True)
    subjectTopic = models.ForeignKey(Topic, null=True, blank=True)
    genreForm = models.CharField(max_length=200, blank=True)

    formatPhysicalX = models.CharField(max_length=200, blank=True)
    formatStandard = models.CharField(max_length=200, blank=True)
    carrierFormat = models.CharField(max_length=200, blank=True)
    carrierId = models.CharField(max_length=200, blank=True)
    carrierPartNumber = models.CharField(max_length=200, blank=True)
    carrierAdditionalPhysicalDescription = models.CharField(max_length=200, blank=True)
    carrierCondition = models.CharField(max_length=200, blank=True)
    carrierAssessedDate = models.CharField(max_length=200, blank=True)
        
    def __unicode__(self):
        return self.title
    
class DigitalFile(models.Model):
    fileName = models.CharField(max_length=200)
    master = models.ForeignKey(Item)
