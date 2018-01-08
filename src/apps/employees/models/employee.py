from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from apps.contacts.mixins import ContactMixin

__all__ = [
    'Employee'
]


def current_date():
    return timezone.now().date()


class Employee(ContactMixin, models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='employee')
    first_name = models.CharField(_('first name'), max_length=128)
    last_name = models.CharField(_('last name'), max_length=128)
    middle_name = models.CharField(
        _('middle name'), default='', max_length=128, blank=True
    )
    notes = models.TextField(_('notes'), default='', blank=True)
    birthday = models.DateField(
        _('birthday'), default=None, null=True, blank=True
    )
    specializations = models.ManyToManyField(
        'employees.Specialization', verbose_name=_('specializations'),
        related_name='employees', blank=True
    )
    position = models.ForeignKey(
        'employees.Position', related_name='employees',
        verbose_name=_('position'),
    )
    work_started = models.DateField(_('work started'), default=current_date)

    def __str__(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')

