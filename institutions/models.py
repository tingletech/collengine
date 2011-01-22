from djangotoolbox.fields import ListField, SetField, DictField, EmbeddedModelField
from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=200)
    ark = models.CharField(max_length=40)
    editors = ListField(models.CharField(max_length=50), blank=True)
    
    def __unicode__(self):
        return self.name

