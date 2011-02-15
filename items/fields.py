from djangotoolbox.fields import ListField, AbstractIterableField

class MyListField(ListField):
    def formfield(self, **kwargs):
        return super(AbstractIterableField, self).formfield(**kwargs)
