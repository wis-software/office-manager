from apps.contacts.models import BaseContact


class ContactMixin(object):

    def get_contacts(self, is_primary=False):
        """


        :param is_primary:
        :return:
        """
        subclasses = BaseContact.__subclasses__()
        results = {}
        for cls in subclasses:
            queryset = cls.objects.filter(employee=self)
            key, verbose = cls.CONTACT_EXTRA_DATA
            if is_primary:
                queryset = queryset.is_primary = True
            results.setdefault(key, queryset)
        return results#.items()
