from django.test import TestCase
from django.contrib.auth.models import User

from apps.employees.models import Employee, Position
from apps.library.models import Holder, Book
from apps.library.tests.graphql_helper import GraphQLHelper


class HoldersTest(TestCase):
    """
    Would be used for testing GraphQL queries
    """
    def __init__(self, *args, **kwargs):
        super(HoldersTest, self).__init__(*args, **kwargs)
        self._holder = {
            'notes': 'test note',
        }

    def setUp(self):
        self._graphql_helper = GraphQLHelper()
        user = User.objects.create_user(username='test', password='secret', email='email@domain.com')
        self._book = Book.objects.create(name='book name', author='author', publisher='publisher')
        position = Position.objects.create(name='name')
        self._employee = Employee.objects.create(first_name='firstName', last_name='lastName', position=position, user=user)
        self._holder_obj = Holder.objects.create(**self._holder, book=self._book, employee=self._employee)

    def test_get_holder(self):
        resp = self._graphql_helper.query('{ holders{ notes} }')
        self._graphql_helper.assertResponseNoErrors(resp['data']['holders'][0], self._holder)

    def test_total_holders(self):
        resp = self._graphql_helper.query('{ totalHolders }')
        self.assertEqual(resp['data']['totalHolders'], Holder.objects.all().count())

    def test_create_holder_successful(self):
        resp = self._graphql_helper.query(
            f'''
            mutation holderCreate{{
                holderCreate(newHolder:{{notes:"note", employee:{self._employee.id}, book:{self._book.id}}}){{
                    ok
                    errors{{
                        field
                        messages
                    }}
                }}
            }}
            '''
        )
        self.assertEqual(resp['data']['holderCreate']['ok'], True)

    def test_create_holder_failed(self):
        resp = self._graphql_helper.query(
            '''
            mutation holderCreate{
                holderCreate(newHolder:{notes:"note", employee:0, book:0}){
                    ok
                }
            }
            '''
        )
        self.assertEqual(resp['data']['holderCreate']['ok'], False)

    def test_create_holder_failed_author_reason(self):
        resp = self._graphql_helper.query(
            '''
            mutation holderCreate{
                holderCreate(newHolder:{notes:"note", employee:0, book:0}){
                    errors{
                        field
                        messages
                    }
                }
            }
            '''
        )
        self.assertEqual(resp['data']['holderCreate']['errors'][0]['field'], 'employee')

    def test_update_holder_successful(self):
        resp = self._graphql_helper.query(
            f'''
            mutation holderUpdate{{
                holderUpdate(newHolder:{{id:{self._holder_obj.id}, notes: "newNote"}}){{
                    ok
                }}
            }}
            '''
        )
        self.assertEqual(resp['data']['holderUpdate']['ok'], True)

    def test_update_holder_notes(self):
        resp = self._graphql_helper.query(
            f'''
            mutation holderUpdate{{
                holderUpdate(newHolder:{{id:{self._holder_obj.id}, notes: "newNote"}}){{
                    holder{{
                        notes
                    }}
                    ok
                    errors{{
                        field
                        messages
                    }}
                }}
            }}
            '''
        )
        self.assertEqual(resp['data']['holderUpdate']['holder']['notes'], "newNote")

    def test_delete_holder(self):
        resp = self._graphql_helper.query(
            f'''
            mutation holderDelete {{
                holderDelete(id:{self._holder_obj.id}) {{
                    ok
                }}
            }}
            '''
        )
        self.assertEqual(resp['data'], {'holderDelete': {'ok': True}})
