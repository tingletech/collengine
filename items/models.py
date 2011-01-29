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
    # 1 Descriptive + Technical
    title = models.CharField(max_length=255)
    contributor = models.ForeignKey(Institution)
    projectId = models.CharField(max_length=255)
    localId = models.CharField(max_length=255)
    aggregatorId = models.CharField(max_length=255)
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
    runningSpeed = models.CharField(max_length=255)
    totalReels = models.IntegerField()
    formatGeneration = models.CharField(max_length=4, choices=GENERATION_CHOICES)
    formatDuration = models.CharField(max_length=255)
    fileNameUniquePart = models.CharField(max_length=255)

    # 2 Additional Descriptive
    alternativeTitle = models.CharField(max_length=255, blank=True)
    seriesTitle = models.CharField(max_length=255, blank=True)
    contributorEditor = models.CharField(max_length=255, blank=True)
    contributorCamera = models.CharField(max_length=255, blank=True)
    contributorSound = models.CharField(max_length=255, blank=True)
    contributorMusic = models.CharField(max_length=255, blank=True)
    contributorCast = models.CharField(max_length=255, blank=True) 
    contributorMusician = models.CharField(max_length=255, blank=True)
    contributorPublisher = models.CharField(max_length=255, blank=True)
    contributorDistributor = models.CharField(max_length=255, blank=True)
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
    genreForm = models.CharField(max_length=255, blank=True)

    # 4 additional technical 
    stockManufacturer = models.CharField(max_length=255, blank=True)
    formatStandard = models.CharField(max_length=4, blank=True, choices=VIDEO_STANDARD_CHOICES)
    carrierFormat = models.CharField(max_length=4, blank=True, choices=VIDEO_ENCODING_CHOICES)
    carrierId = models.CharField(max_length=255, blank=True)
    carrierPartNumber = models.CharField(max_length=255, blank=True)
    carrierAdditionalPhysicalDescription = models.CharField(max_length=255, blank=True)
    carrierCondition = models.CharField(max_length=255, blank=True)
    carrierAssessedDate = models.DateField(null=True, blank=True)

    # 6 Rights
    #copyrightStatus
    #[autogenerate statements based on template somehow]
    #copyrightHolder
    #copyrightHolder Info
    #copyrightDate
    #copyrightNotice
        
    def __unicode__(self):
        return self.title
    
class DigitalFile(models.Model):
    # 3 Technical
    fileName = models.CharField(max_length=255)
    master = models.ForeignKey(Item)
    state = models.CharField(max_length=4, choices=STATE_CHOICES)
    formatDigital = models.CharField(max_length=4, choices=DIGITAL_CHOICES)
    formatDigitalLocation = models.CharField(max_length=255)
    # formatPhysical medium manufacturer & model (?) # still think this sounds like a property of the tape / pyhsical media
    formatPhysicalStorageMedium = models.CharField(max_length=255)
    formatDefinition = models.CharField(max_length=4, choices=DEFINITION_CHOICES)
    # formatStandard + version
    fourCC = models.CharField(max_length=4)			# http://www.fourcc.org/codecs.php

    # formatEncoding	255 char
    # codecQuality	lossless -- lossy
    #formatDataRate	integer (in Mbps)
    #formatBitDepth	10 bit -- 8 bit
    #formatSamplingRate	fixed -- variable
    #formatFileSize	integer 
    #formatTimeStart	timecode
    #sampleRatio	ratio of integers
    #formatFrameSize	525 -- 625 -- 720 -- 1080
    #formatAspectRatio	ratio of integers
    #formatFrameRate	integer
    #fileCreated	date
    #formatFrameSize	integer (in pixels per line)
    #formatChannelConfiguration	255 char
    #soundChannels	integer
    #soundLinear	sound linear -- embedded -- both
    #soundAnnotation	mono -- stereo -- surround
    #mixType	music -- dialogue and music -- interview -- field recording
    #offloadDate	date
    #

    # 5 Provenance + Preservation
    # this block is all opitonal
    #sourceDeck	255 char
    #digitizer	255 char
    #encodingApplication	255 char
    #transferHardware	255 char
    #transferSoftware	255 char
    #Processing hardware	255 char
    #Processing software	255 char
    #transferVendor	255 char
    #transferOperator	255 char
    #transferDate	date
    #transferNotes	255 char
    #checksum	integer
    #checksumKind	MD5
    #checksumDate	date
    #renderingHardware	255 char
    #renderingSoftware	255 char
    #fileValidationSoftware	JHOVE2 -- Terminal
    #qualityControlComments	255 char
    #qualityControlDate	date
    #qualityControlInitials	255 char
    #qualityControlActions	255 char
    #additionalEvent	Ingested -- Migrated -- Backed-up -- Obsolescence rating
    #additionalEventNotes	255 char
    #viewingEnvironment	255 char
    
    def __unicode__(self):
        return self.fileName
