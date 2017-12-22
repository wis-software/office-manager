from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    'Specialization'
]


class Specialization(models.Model):
    name = models.CharField(_('name'), max_length=512, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = _('specialization')
