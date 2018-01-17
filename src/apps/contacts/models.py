from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseContact(models.Model):
    employee = models.ForeignKey('employees.Employee',
                                 verbose_name=_('employee'),
                                 related_name='%(class)s_contact_list')
    is_primary = models.BooleanField(_('is primary'), default=False)
    is_active = models.BooleanField(_('is active'), default=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        abstract = True


class Skype(BaseContact):
    CONTACT_EXTRA_DATA = ('skype', _('Skype accounts'))

    login = models.CharField(_('skype login'), max_length=32)

    class Meta:
        verbose_name = _('skype account')
        verbose_name_plural = _('skype accounts')


class Email(BaseContact):
    CONTACT_EXTRA_DATA = ('email', _('Emails'))

    email = models.EmailField(_('email'))

    class Meta:
        verbose_name = _('email')
        verbose_name_plural = _('emails')


class PhoneNumber(BaseContact):
    CONTACT_EXTRA_DATA = ('phone_number', _('Phone numbers'))

    number = models.CharField(_('number'), max_length=32)

    class Meta:
        verbose_name = _('phone number')
        verbose_name_plural = _('phone numbers')


class GitAccount(BaseContact):
    CONTACT_EXTRA_DATA = ('git', _('Git accounts'))

    account = models.CharField(_('number'), max_length=32)
    url = models.CharField(_('url'), max_length=32)

    class Meta:
        verbose_name = _('phone number')
        verbose_name_plural = _('phone numbers')
