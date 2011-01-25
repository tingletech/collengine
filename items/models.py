from djangotoolbox.fields import ListField, SetField, DictField, EmbeddedModelField
from institutions.models import Institution
from archival_collections.models import Collection
from vocabularies.models import Name, Place, Topic
from django.db import models
from django.contrib import admin

# Create your models here.

MEDIATYPE_CHOICES = ( 'moving image', 'sound',)

PHYSICAL_X_CHOICES = ( 
  '1/4" audiocassette',
  '1/4" audio open reel',
  '1/2" video open reel',
  '35 mm film',
  '16 mm film',
  '8 mm film',
  'Super 8 mm film',
)

SOUND_CHARACTERISTICS_CHOICES = ( 'sound', 'silent',)

COLORS_CHOICES = ( 'color', 'black & white',)

GENERATION_CHOICES = (
  'camera original', 
  'master',
  'submaster'
  'unknown'
)

STATE_CHOICES = (
  'preservation master',
  'production master',
  'mezzanine/copy master',
  'access derivative',
)

DIGITAL_CHOICES = (
  'uncompressed .mov',
  'dv5',
  'MPEG4',
  'broadcast wave',
  'MP3',
)

STORAGE_MEDIUM_CHOICES = (
  'server',
  'HDD',
  'DVD',
)

DEFINITION_CHOICES = (
  'Standard Definition (SD)',
  'High Definition (HD)',
)

CODECQUALITY_CHOICES = (
  'lossless',
  'lossy',
)

BITDEPTH_CHOICES = (
  '10 bit',
  '8 bit',
)

SAMPLING_RATE_CHOICES = (
  'fixed',
  'variable',
)

FRAMESIZE_CHOICES = (
  '525',
  '625',
  '720',
  '1080',
)

SOUND_LINEAR_CHOICES = (
  'sound linear',
  'embedded',
  'both',
)

SOUND_ANNOTATION_CHOICES = (
  'mono',
  'stereo',
  'surround',
)

MIX_TYPE_CHOICES = (
  'music',
  'dialogue and music',
  'interview',
  'field recording',
)

VIDEO_STANDARD_CHOICES = (
  'NTSC',
  'PAL',
)

VIDEO_ENCODING_CHOICES = (
  'composite',
  'component',
)

VALIDATION_SOFTWARE_CHOICES = (
  'JHOVE2',
  'Terminal',
)

EVENT_CHOICES = (
  'Ingested',
  'Migrated',
  'Backed-up',
  'Obsolescence rating',
)

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
