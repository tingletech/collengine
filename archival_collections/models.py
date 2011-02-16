from djangotoolbox.fields import ListField, SetField, DictField, EmbeddedModelField
from django.db import models

# model for archivally controlled collection

class Collection(models.Model):
    name = models.CharField(max_length=200)
    ark = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return self.name
