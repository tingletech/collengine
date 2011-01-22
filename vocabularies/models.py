from djangotoolbox.fields import ListField, SetField, DictField, EmbeddedModelField
from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
