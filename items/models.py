from djangotoolbox.fields import ListField, SetField, DictField, EmbeddedModelField
from institutions.models import Institution
from archival_collections.models import Collection
from vocabularies.models import Name, Place, Topic
from django.db import models
from django.contrib import admin

# Create your models here.

MEDIA_TYPE_CHOICES = ( 
  ('movi', 'moving image', ),
  ('soun', 'sound',),
)

PHYSICAL_FORMAT_CHOICES = ( 
  ('4ac', '1/4" audiocassette',),
  ('4aor', '1/4" audio open reel',),
  ('2vor', '1/2" video open reel',),
  ('35fl', '35 mm film',),
  ('16fl', '16 mm film',),
  ('8fl', '8 mm film',),
  ('s8fl', 'Super 8 mm film',),
)

SOUND_CHARACTERISTICS_CHOICES = ( 
  ('soun', 'sound', ),
  ('sile','silent',)
)

COLORS_CHOICES = ( 
  ('colo', 'color', ),
  ('b&w', 'black & white',),
)

GENERATION_CHOICES = (
  ('orig', 'camera original', ),
  ('mast', 'master',),
  ('subm', 'submaster'),
  ('unkn', 'unknown'),
)

STATE_CHOICES = (
  ('pres', 'preservation master',),
  ('prod', 'production master',),
  ('mezz', 'mezzanine/copy master',),
  ('acce', 'access derivative',),
)

DIGITAL_CHOICES = (
  ('umov', 'uncompressed .mov',),
  ('dv5', 'dv5',),
  ('mpg4', 'MPEG4',),
  ('bwav', 'broadcast wave',),
  ('mp3', 'MP3',),
)

STORAGE_MEDIUM_CHOICES = (
  ('serv', 'server',),
  ('HDD', 'HDD',),
  ('DVD', 'DVD',),
)

DEFINITION_CHOICES = (
  ('SD', 'Standard Definition (SD)',),
  ('HD', 'High Definition (HD)',),
)

CODECQUALITY_CHOICES = (
  ('less', 'lossless',),
  ('loss', 'lossy',),
)

BITDEPTH_CHOICES = (
  ('10b', '10 bit',),
  ('8b', '8 bit',),
)

SAMPLING_RATE_CHOICES = (
  ('fix', 'fixed',),
  ('var', 'variable',),
)

FRAMESIZE_CHOICES = (
  ('525', '525',),
  ('625', '625',),
  ('720', '720',),
  ('1080', '1080',),
)

SOUND_LINEAR_CHOICES = (
  ('slin', 'sound linear',),
  ('embe', 'embedded',),
  ('both', 'both',),
)

SOUND_ANNOTATION_CHOICES = (
  ('mono', 'mono',),
  ('ster', 'stereo',),
  ('surr', 'surround',),
)

MIX_TYPE_CHOICES = (
  ('musi', 'music',),
  ('d+m', 'dialogue and music',),
  ('inte', 'interview',),
  ('fiel', 'field recording',),
)

VIDEO_STANDARD_CHOICES = (
  ('NTSC', 'NTSC',),
  ('PAL', 'PAL',),
)

VIDEO_ENCODING_CHOICES = (
  ('site', 'composite',),
  ('nent', 'component',),
)

VALIDATION_SOFTWARE_CHOICES = (
  ('jhov', 'JHOVE2',),
  ('term', 'Terminal',),
)

EVENT_CHOICES = (
  ('in', 'Ingested',),
  ('migr', 'Migrated',),
  ('back', 'Backed-up',),
  ('rate', 'Obsolescence rating',),
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
    formatMediaType = models.CharField(max_length=4, choices=MEDIA_TYPE_CHOICES)
    physicalFormat = models.CharField(max_length=4, choices=PHYSICAL_FORMAT_CHOICES)
    silent = models.CharField(max_length=4, choices=SOUND_CHARACTERISTICS_CHOICES)
    formatColors = models.CharField(max_length=4, choices=COLORS_CHOICES)
    runningSpeed = models.CharField(max_length=200)
    totalReels = models.IntegerField()
    formatGeneration = models.CharField(max_length=4, choices=GENERATION_CHOICES)
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

    stockManufacturer = models.CharField(max_length=200, blank=True)
    formatStandard = models.CharField(max_length=4, blank=True, choices=VIDEO_STANDARD_CHOICES)
    carrierFormat = models.CharField(max_length=4, blank=True, choices=VIDEO_ENCODING_CHOICES)
    carrierId = models.CharField(max_length=200, blank=True)
    carrierPartNumber = models.CharField(max_length=200, blank=True)
    carrierAdditionalPhysicalDescription = models.CharField(max_length=200, blank=True)
    carrierCondition = models.CharField(max_length=200, blank=True)
    carrierAssessedDate = models.DateField(null=True, blank=True)
        
    def __unicode__(self):
        return self.title
    
class DigitalFile(models.Model):
    fileName = models.CharField(max_length=200)
    master = models.ForeignKey(Item)
