from django.test import TestCase

from apps.library.models import Book
from apps.library.tests.graphql_helper import GraphQLHelper


class BooksTest(TestCase):
    """
    Would be used for testing GraphQL queries
    """
    def __init__(self, *args, **kwargs):
        super(BooksTest, self).__init__(*args, **kwargs)
        self._book = {
            'name': 'test name',
            'author': 'test author',
            'publisher': 'test'
        }

    def setUp(self):
        self._graphql_helper = GraphQLHelper()
        self._book_obj = Book.objects.create(**self._book)

    def test_get_book(self):
        resp = self._graphql_helper.query('{ books{ name, author, publisher } }')
        self._graphql_helper.assertResponseNoErrors(resp['data']['books'][0], self._book)

    def test_total_books(self):
        resp = self._graphql_helper.query('{ totalBooks }')
        self.assertEqual(resp['data']['totalBooks'], Book.objects.all().count())

    def test_create_book_successful(self):
        resp = self._graphql_helper.query(
            '''
            mutation bookCreate{
                bookCreate(newBook:{name: "book2 name", author: "name", publisher: "name"}){
                    ok
                }
            }
            '''
        )
        self.assertEqual(resp['data']['bookCreate']['ok'], True)

    def test_create_book_failed(self):
        resp = self._graphql_helper.query(
            '''
            mutation bookCreate{
                bookCreate(newBook:{name: "book2 name", author: "", publisher: "name"}){
                    ok
                }
            }
            '''
        )
        self.assertEqual(resp['data']['bookCreate']['ok'], False)

    def test_create_book_failed_author_reason(self):
        resp = self._graphql_helper.query(
            '''
            mutation bookCreate{
                bookCreate(newBook:{name: "book2 name", author: "", publisher: "name"}){
                    errors{
                        field
                        messages
                    }
                }
            }
            '''
        )
        self.assertEqual(resp['data']['bookCreate']['errors'][0]['field'], 'author')

    def test_create_book_check_name(self):
        resp = self._graphql_helper.query(
            '''
            mutation bookCreate{
                bookCreate(newBook:{name: "book3 name", author: "name", publisher: "name"}){
                    book{
                        name
                    }
                }
            }
            '''
        )
        self.assertEqual(resp['data']['bookCreate']['book']['name'], "book3 name")

    def test_update_book_successful(self):
        resp = self._graphql_helper.query(
            f'''
            mutation bookUpdate{{
                bookUpdate(newBook:{{id:{self._book_obj.id}, name: "newName"}}){{
                    ok
                }}
            }}
            '''
        )

        self.assertEqual(resp['data']['bookUpdate']['ok'], True)

    def test_update_book_failed(self):
        resp = self._graphql_helper.query(
            f'''
            mutation bookUpdate{{
                bookUpdate(newBook:{{id:{self._book_obj.id}, name: "newName",  author: ""}}){{
                    ok
                }}
            }}
            '''
        )

        self.assertEqual(resp['data']['bookUpdate']['ok'], False)

    def test_update_book_failed_author_reason(self):
        resp = self._graphql_helper.query(
            f'''
            mutation bookUpdate{{
                bookUpdate(newBook:{{id:{self._book_obj.id}, name: "newName", author: ""}}){{
                    errors{{
                        field
                        messages
                    }}
                }}
            }}
            '''
        )

        self.assertEqual(resp['data']['bookUpdate']['errors'][0]['field'], 'author')

    def test_update_book_name(self):
        resp = self._graphql_helper.query(
            f'''
            mutation bookUpdate{{
                bookUpdate(newBook:{{id:{self._book_obj.id}, name: "newName"}}){{
                    book{{
                        name
                    }}
                }}
            }}
            '''
        )
        self.assertEqual(resp['data']['bookUpdate']['book']['name'], "newName")

    def test_delete_book(self):
        resp = self._graphql_helper.query(
            f'''
            mutation bookDelete{{
                bookDelete(id:{self._book_obj.id}){{
                    ok
                }}
            }}
            '''
        )
        self.assertEqual(resp['data'], {'bookDelete': {'ok': True}})
