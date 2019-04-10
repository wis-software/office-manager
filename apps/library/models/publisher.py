from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    'Publisher'
]


class Publisher(models.Model):
    title = models.CharField(_('name'), max_length=1024)
    description = models.TextField(_('description'), default='', blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('publisher')
        verbose_name_plural = _('publishers')
