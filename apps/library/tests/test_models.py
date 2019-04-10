from django.test import TestCase

from apps.library.models import Book, Holder, Offer, Tag, Author, Publisher
from apps.employees.models import Employee

from model_mommy import mommy


class BookModelTest(TestCase):

    def setUp(self):
        self.book = mommy.make(Book)

    def test_string_representation(self):
        self.assertEqual(str(self.book), self.book.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Book._meta.verbose_name_plural), 'books')

    def test_kind_book_create_instance(self):
        self.assertIsInstance(self.book, Book)


class HolderModelTest(TestCase):

    def setUp(self):
        self.holder = mommy.make(Holder)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Holder._meta.verbose_name_plural), 'holders')

    def test_kind_holder_create_instance(self):
        self.assertIsInstance(self.holder, Holder)


class OfferModelTest(TestCase):

    def setUp(self):
        self.employee = mommy.make(Employee)
        self.offer = mommy.make(Offer, employee=self.employee)

    def test_string_name_representation(self):
        self.assertEqual(str(self.offer), self.offer.name)

    def test_string_url_representation(self):
        offer_without_name = mommy.make(Offer, name='')
        self.assertEqual(str(offer_without_name), offer_without_name.url)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Offer._meta.verbose_name_plural), 'offers')

    def test_kind_offer_create_instance(self):
        self.assertIsInstance(self.offer, Offer)

    def test_offer_employee(self):
        self.assertEqual(self.employee, self.offer.employee)


class TagModelTest(TestCase):

    def setUp(self):
        self.tag = mommy.make(Tag)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Tag._meta.verbose_name_plural), 'tags')

    def test_kind_offer_create_instance(self):
        self.assertIsInstance(self.tag, Tag)


class AuthorModelTest(TestCase):

    def setUp(self):
        self.author = mommy.make(Author)

    def test_string_representation(self):
        self.assertEqual(str(self.author), self.author.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Author._meta.verbose_name_plural), 'authors')

    def test_kind_author_create_instance(self):
        self.assertIsInstance(self.author, Author)


class PublisherModelTest(TestCase):

    def setUp(self):
        self.publisher = mommy.make(Publisher)

    def test_string_representation(self):
        self.assertEqual(str(self.publisher), self.publisher.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Publisher._meta.verbose_name_plural), 'publishers')

    def test_kind_publisher_create_instance(self):
        self.assertIsInstance(self.publisher, Publisher)
