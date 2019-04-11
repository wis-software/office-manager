from django.test import TestCase
from django.contrib.auth.models import User

from apps.library.models import Offer, Book
from apps.employees.models import Employee, Position
from apps.library.tests.graphql_helper import GraphQLHelper


class OffersTest(TestCase):
    """
    Would be used for testing GraphQL queries
    """
    def __init__(self, *args, **kwargs):
        super(OffersTest, self).__init__(*args, **kwargs)
        self._offer = {
            'name': 'test name',
            'price': 100,
            'count': 1
        }

    def setUp(self):
        self._graphql_helper = GraphQLHelper()
        book = Book.objects.create(name='book name', author='author', publisher='publisher')
        user = User.objects.create_user(username='test', password='secret', email='email@domain.com')
        position = Position.objects.create(name='name')
        employee = Employee.objects.create(first_name='firstName', last_name='lastName', position=position, user=user)

        self._offer_obj = Offer.objects.create(**self._offer, book=book, employee=employee)

    def test_get_offer(self):
        resp = self._graphql_helper.query('{ offers{ name, price, count} }')
        self._graphql_helper.assertResponseNoErrors(resp['data']['offers'][0], self._offer)

    def test_total_offers(self):
        resp = self._graphql_helper.query('{ totalOffers }')
        self.assertEqual(resp['data']['totalOffers'], Offer.objects.all().count())

    # def test_create_offer_successful(self):
    #     resp = self._graphql_helper.query(
    #         '''
    #         mutation offerCreate{
    #             offerCreate(newOffer:{name: "offer2 name"}){
    #                 ok
    #             }
    #         }
    #         '''
    #     )
    #     self.assertEqual(resp['data']['offerCreate']['ok'], True)
    #
    # def test_create_offer_failed(self):
    #     resp = self._graphql_helper.query(
    #         '''
    #         mutation offerCreate{
    #             offerCreate(newOffer:{name: "offer2 name", author: "", publisher: "name"}){
    #                 ok
    #             }
    #         }
    #         '''
    #     )
    #     self.assertEqual(resp['data']['offerCreate']['ok'], False)
    #
    # def test_create_offer_failed_author_reason(self):
    #     resp = self._graphql_helper.query(
    #         '''
    #         mutation offerCreate{
    #             offerCreate(newOffer:{name: "offer2 name", author: "", publisher: "name"}){
    #                 errors{
    #                     field
    #                     messages
    #                 }
    #             }
    #         }
    #         '''
    #     )
    #     self.assertEqual(resp['data']['offerCreate']['errors'][0]['field'], 'author')
    #
    # def test_create_offer_check_name(self):
    #     resp = self._graphql_helper.query(
    #         '''
    #         mutation offerCreate{
    #             offerCreate(newOffer:{name: "offer3 name", author: "name", publisher: "name"}){
    #                 offer{
    #                     name
    #                 }
    #             }
    #         }
    #         '''
    #     )
    #     self.assertEqual(resp['data']['offerCreate']['offer']['name'], "offer3 name")
    #
    def test_update_offer_successful(self):
        resp = self._graphql_helper.query(
            f'''
            mutation offerUpdate{{
                offerUpdate(newOffer:{{id:{self._offer_obj.id}, name: "newName"}}){{
                    ok
                }}
            }}
            '''
        )
        self.assertEqual(resp['data']['offerUpdate']['ok'], True)

    def test_update_offer_name(self):
        resp = self._graphql_helper.query(
            f'''
            mutation offerUpdate{{
                offerUpdate(newOffer:{{id:{self._offer_obj.id}, name: "newName"}}){{
                    offer{{
                        name
                    }}
                }}
            }}
            '''
        )
        self.assertEqual(resp['data']['offerUpdate']['offer']['name'], "newName")

    def test_update_offer_failed(self):
        resp = self._graphql_helper.query(
            f'''
            mutation offerUpdate{{
                offerUpdate(newOffer:{{id:{self._offer_obj.id}, count: -1}}){{
                    ok
                }}
            }}
            '''
        )

        self.assertEqual(resp['data']['offerUpdate']['ok'], False)

    def test_update_offer_failed_author_reason(self):
        resp = self._graphql_helper.query(
            f'''
            mutation offerUpdate{{
                offerUpdate(newOffer:{{id:{self._offer_obj.id}, count: -1}}){{
                    errors{{
                        field
                        messages
                    }}
                }}
            }}
            '''
        )

        self.assertEqual(resp['data']['offerUpdate']['errors'][0]['field'], 'count')

    def test_delete_offer(self):
        resp = self._graphql_helper.query(
            f'''
            mutation offerDelete {{
                offerDelete(id:{self._offer_obj.id}) {{
                    ok
                }}
            }}
            '''
        )
        self.assertEqual(resp['data'], {'offerDelete': {'ok': True}})
