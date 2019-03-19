from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    'Book'
]


class Book(models.Model):
    name = models.CharField(_('name'), max_length=1024)
    authors = models.ManyToManyField('library.Author', verbose_name=_('authors'),
                                  blank=False, related_name='books')
    publishers = models.ManyToManyField('library.Publisher', verbose_name=_('publishers'),
                                        blank=True, related_name='books')
    description = models.TextField(_('description'), default='', blank=True)
    tags = models.ManyToManyField('library.Tag', verbose_name=_('tags'),
                                  blank=True, related_name='books')
    specializations = models.ManyToManyField('employees.specialization',
                                             blank=True, related_name='books',
                                             verbose_name=_('specializations'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
