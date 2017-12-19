from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = [
    'Specialization'
]


class Specialization(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=512, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _('specialization')
