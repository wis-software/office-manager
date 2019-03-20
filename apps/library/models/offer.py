from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    'Offer'
]


class Offer(models.Model):
    book = models.OneToOneField('library.Book', blank=True, default=None,
                                verbose_name=_('book'), related_name='offer',
                                null=True)
    employee = models.ForeignKey('employees.Employee',
                                 verbose_name=_('employee'),
                                 related_name='book_offers')
    name = models.CharField(_('name'), max_length=512, default='', blank=True)
    url = models.CharField(_('url'), max_length=512, default='', blank=True)
    price = models.IntegerField(_('price'), default=0)
    count = models.PositiveIntegerField(_('count'), default=1)
    description = models.TextField(_('description'), default='', blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return self.name or self.url

    class Meta:
        verbose_name = _('offer')
        verbose_name_plural = _('offers')
