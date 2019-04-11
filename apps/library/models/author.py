from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    'Author'
]

class Author(models.Model):
    name = models.CharField(_('name'), max_length=1024)
    about = models.TextField(_('about'), default='', blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
