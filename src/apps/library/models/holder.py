from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    'Holder'
]


class Holder(models.Model):
    employee = models.ForeignKey('employees.Employee',
                                 verbose_name=_('employee'),
                                 related_name='holder_history')
    book = models.ForeignKey('library.Book', related_name='holder_history',
                             verbose_name=_('book'))
    notes = models.TextField(_('notes'), default='', blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    refunded_at = models.DateTimeField(_('refunded at'), null=True, blank=True)

    class Meta:
        verbose_name = _('holder')
        verbose_name_plural = _('holders')
