from djangotoolbox.fields import ListField, AbstractIterableField

class MyListField(ListField):
    def formfield(self, **kwargs):
        # The search order is same as that used by getattr() except that the type itself is skipped.
        # http://docs.python.org/library/functions.html#super
        return super(AbstractIterableField, self).formfield(**kwargs)
