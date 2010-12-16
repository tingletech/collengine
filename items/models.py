from djangotoolbox.fields import ListField, SetField, DictField, EmbeddedModelField
from django.db import models

# Create your models here.

class Institution(models.Model):
    label = models.CharField(max_length=200)
    ark = models.CharField(max_length=40)
    editors = ListField(models.CharField(max_length=50))
    
    def __unicode__(self):
        return self.label

class Collection(models.Model):
    label = models.CharField(max_length=200)
    ark = models.CharField(max_length=40)

    def __unicode__(self):
        return self.label

class Item(models.Model):
    DC_TYPES = (
        (u'Collection', u'Collection'),
        (u'Dataset', u'Dataset'),
        (u'Event', u'Event'),
        (u'Image', u'Image'),
        (u'InteractiveResource', u'Interactive Resource'),
        (u'MovingImage', u'Moving Image'),
        (u'PhysicalObject', u'Physical Object'),
        (u'Service', u'Service'),
        (u'Software', u'Software'),
        (u'Sound', u'Sound'),
        (u'StillImage', u'Still Image'),
        (u'Text', u'Text'),
    )
    contributor = ListField(models.CharField(max_length=200))
    coverage = ListField(models.CharField(max_length=200))
    creator = ListField(models.CharField(max_length=200))
    date = ListField(models.CharField(max_length=200))
    description = ListField(models.TextField())
    format = ListField(models.CharField(max_length=200))
    identifier = ListField(models.CharField(max_length=200))
    ark_identifier = models.CharField(max_length=50)
    language = ListField(models.CharField(max_length=200))
    publisher = ListField(models.CharField(max_length=200))
    courtesy_of_publisher = models.ForeignKey(Institution)
    relation = ListField(models.CharField(max_length=200))
    relation_parent_collection = models.ForeignKey(Collection)
    rights = ListField(models.CharField(max_length=200))
    source = ListField(models.CharField(max_length=200))
    subject = ListField(models.CharField(max_length=200))
    title = ListField(models.CharField(max_length=200))
    type = models.CharField(max_length=2, choices=DC_TYPES)

    def __unicode__(self):
        return self.label
