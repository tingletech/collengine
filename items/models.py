#from djangotoolbox.fields import ListField, SetField, DictField, EmbeddedModelField
from .fields import MyListField as ListField
from institutions.models import Institution
from archival_collections.models import Collection
from vocabularies.models import Name, Place, Topic
from django.db import models
from django.contrib import admin


# Create your models here.

# hardcoded controlled vocabularies

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

CODEC_QUALITY_CHOICES = (
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
    title = models.CharField(max_length=255, help_text="help text blah blah")
    contributor = models.ForeignKey(Institution)
    projectId = models.CharField(max_length=255)
    localId = models.CharField(max_length=255)
    aggregatorId = models.CharField(max_length=255)
    creatorWriter = ListField(models.ForeignKey(Name, related_name="writer", null=True, blank=True), null=True, blank=True)
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

    formatEncoding = models.CharField(max_length=255)
    codecQuality = models.CharField(max_length=4, choices=CODEC_QUALITY_CHOICES)
    # formatDataRate	integer (in Mbps)
    formatDataRate = models.CharField(max_length=255)
    # integer won't work, see http://www.pbcore.org/PBCore/formatDataRate.html
    #      models.DecimalField(..., max_digits=5, decimal_places=2)
    formatBitDepth = models.CharField(max_length=4, choices=BITDEPTH_CHOICES)
    formatSamplingRate = models.CharField(max_length=4, choices=SAMPLING_RATE_CHOICES)
    fileSizeBytes = models.IntegerField()
    formatTimeStart = models.CharField(max_length=25)
    sampleRatioNumerator = models.IntegerField()
    sampleRatioDenominator = models.IntegerField()
    formatFrameSize = models.CharField(max_length=4, choices=FRAMESIZE_CHOICES)
    formatAspectRatioNumerator = models.IntegerField()
    formatAspectRatioDenominator = models.IntegerField()
    #formatFrameRate	integer; no see http://www.pbcore.org/PBCore/formatFrameRate.html ss picklist
    formatFrameRate = models.CharField(max_length=255)
    fileCreated = models.DateField(null=True, blank=True)
    # formatFrameSize	integer (in pixels per line) no; 
    #     see http://www.pbcore.org/PBCore/formatFrameSize.html ss picklist
    formatTracks = models.CharField(max_length=255) 
    formatChannelConfiguration = models.CharField(max_length=255) 
    # soundChannels	integer
    # soundLinear	sound linear -- embedded -- both
    # soundAnnotation	mono -- stereo -- surround
    mixType = models.CharField(max_length=4, choices=MIX_TYPE_CHOICES)
    offloadDate = models.DateField(null=True, blank=True)
    #

    # 5 Provenance + Preservation
    # this block is all opitonal
    sourceDeck = models.CharField(max_length=255, blank=True)
    digitizer = models.CharField(max_length=255, blank=True)
    encodingApplication = models.CharField(max_length=255, blank=True)
    transferHardware = models.CharField(max_length=255, blank=True)
    transferSoftware = models.CharField(max_length=255, blank=True)
    processingHardware = models.CharField(max_length=255, blank=True)
    processingSoftware = models.CharField(max_length=255, blank=True)
    transferVendor = models.CharField(max_length=255, blank=True)
    transferOperator = models.CharField(max_length=255, blank=True)
    transferDate = models.DateField(null=True, blank=True)
    transferNotes = models.CharField(max_length=255, blank=True)
    # checksum	integer (checksums are not usually stored or expressed as ints)
    # checksumKind	MD5
    md5Checksum = models.CharField(max_length=255, blank=True)
    checksumDate = models.DateField(null=True, blank=True)
    renderingHardware = models.CharField(max_length=255, blank=True)
    renderingSoftware = models.CharField(max_length=255, blank=True)
    fileValidationSoftware = models.CharField(max_length=4, choices=VALIDATION_SOFTWARE_CHOICES)
    qualityControlComments = models.CharField(max_length=255, blank=True)
    qualityControlDate = models.DateField(null=True, blank=True)
    qualityControlInitials = models.CharField(max_length=255, blank=True)
    qualityControlActions = models.CharField(max_length=255, blank=True)
    additionalEvent = models.CharField(max_length=4, choices=EVENT_CHOICES)
    additionalEventNotes = models.CharField(max_length=255, blank=True)
    viewingEnvironment = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.fileName
