from apps.contacts.models import BaseContact


class ContactMixin(object):
    """
    Would be used for adding contacts functionality to models with contact data.
    """

    def get_contacts(self, is_primary=False):
        """
        Returns dict with all contacts.
        Example:
        >> obj.get_contacts()
        << {'email': [], 'skype': []}

        :param is_primary: bool Return only primary contacts.
        :return: dict
        """
        subclasses = BaseContact.__subclasses__()
        results = {}
        for cls in subclasses:
            queryset = cls.objects.filter(employee_id=self.id)
            key, verbose = cls.CONTACT_EXTRA_DATA
            if is_primary:
                queryset = queryset.filter(is_primary=True)
            results.setdefault(key, queryset)
        return results
