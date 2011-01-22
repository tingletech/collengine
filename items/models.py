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
    creatorWriter = models.ForeignKey(Name, related_name="writer")
    creatorDirector = models.ForeignKey(Name, related_name="director")
    creatorProducer = models.ForeignKey(Name, related_name="producer")
    countryOfCreation = models.CharField(max_length=2)
    dateCreated = models.DateField()
    dateIssued = models.DateField()
    formatMediaType = models.CharField(max_length=200)
    formatPhysicalY = models.CharField(max_length=200)
    silent = models.CharField(max_length=200)
    formatColors = models.CharField(max_length=200)
    runningSpeed = models.CharField(max_length=200)
    totalReels = models.CharField(max_length=200)
    formatGeneration = models.CharField(max_length=200)
    formatDuration = models.CharField(max_length=200)
    fileNameUniquePart = models.CharField(max_length=200)

    alternativeTitle = models.CharField(max_length=200)
    seriesTitle = models.CharField(max_length=200)
    contributorCamera = models.CharField(max_length=200)
    contributorEditor = models.CharField(max_length=200)
    contributorSound = models.CharField(max_length=200)
    contributorMusic = models.CharField(max_length=200)
    contributorCast = models.CharField(max_length=200)
    contributorMusician = models.CharField(max_length=200)
    contributorPublisher = models.CharField(max_length=200)
    contributorDistributor = models.CharField(max_length=200)
    collection = models.ForeignKey(Collection)
    descriptionGeneralNote = models.TextField()
    descriptionAbstract = models.TextField()
    descriptionContents = models.TextField()
    descriptionTranscript = models.TextField()
    descriptionShotList = models.TextField()
    language = models.CharField(max_length=2)
    subjectName = models.ForeignKey(Name, related_name="subject_name")
    subjectPlace = models.ForeignKey(Place)
    subjectTopic = models.ForeignKey(Topic)
    genreForm = models.CharField(max_length=200)

    formatPhysicalX = models.CharField(max_length=200)
    formatStandard = models.CharField(max_length=200)
    carrierFormat = models.CharField(max_length=200)
    carrierId = models.CharField(max_length=200)
    carrierPartNumber = models.CharField(max_length=200)
    carrierAdditionalPhysicalDescription = models.CharField(max_length=200)
    carrierCondition = models.CharField(max_length=200)
    carrierAssessedDate = models.CharField(max_length=200)
        
    def __unicode__(self):
        return self.title
    
class digitalFile(models.Model):
    fileName = models.CharField(max_length=200)
    master = models.ForeignKey(Item)
