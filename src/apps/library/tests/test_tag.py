from django.test import TestCase

from apps.library.models import Tag
from apps.library.tests.graphql_helper import GraphQLHelper


class TagsTest(TestCase):
    """
    Would be used for testing GraphQL queries
    """
    def __init__(self, *args, **kwargs):
        super(TagsTest, self).__init__(*args, **kwargs)
        self._tag = {
            'name': 'test name',
        }

    def setUp(self):
        self._graphql_helper = GraphQLHelper()
        self._tag_obj = Tag.objects.create(**self._tag)

    def test_get_tag(self):
        resp = self._graphql_helper.query('{ tags{ name } }')
        self._graphql_helper.assertResponseNoErrors(resp['data']['tags'][0], self._tag)

    def test_total_tags(self):
        resp = self._graphql_helper.query('{ totalTags }')
        self.assertEqual(resp['data']['totalTags'], Tag.objects.all().count())

    def test_create_tag_successful(self):
        resp = self._graphql_helper.query(
            '''
            mutation tagCreate{
                tagCreate(newTag:{name: "tag2 name"}){
                    ok
                }
            }
            '''
        )

        self.assertEqual(resp['data']['tagCreate']['ok'], True)

    def test_create_tag_failed(self):
        resp = self._graphql_helper.query(
            '''
            mutation tagCreate{
                tagCreate(newTag:{name: ""}){
                    ok
                }
            }
            '''
        )
        self.assertEqual(resp['data']['tagCreate']['ok'], False)

    def test_create_tag_failed_name_reason(self):
        resp = self._graphql_helper.query(
            '''
            mutation tagCreate{
                tagCreate(newTag:{name: ""}){
                    errors{
                        field
                        messages
                    }
                }
            }
            '''
        )
        self.assertEqual(resp['data']['tagCreate']['errors'][0]['field'], 'name')

    def test_create_tag_check_name(self):
        resp = self._graphql_helper.query(
            '''
            mutation tagCreate{
                tagCreate(newTag:{name: "tag3 name"}){
                    tag{
                        name
                    }
                }
            }
            '''
        )
        self.assertEqual(resp['data']['tagCreate']['tag']['name'], "tag3 name")

    def test_update_tag_successful(self):
        resp = self._graphql_helper.query(
            f'''
            mutation tagUpdate{{
                tagUpdate(newTag:{{id:{self._tag_obj.id}, name: "newName"}}){{
                    ok
                    errors{{
                        field
                        messages
                    }}
                }}
            }}
            '''
        )

        self.assertEqual(resp['data']['tagUpdate']['ok'], True)

    def test_update_tag_failed(self):
        resp = self._graphql_helper.query(
            f'''
            mutation tagUpdate{{
                tagUpdate(newTag:{{id:{self._tag_obj.id}, name: ""}}){{
                    ok
                }}
            }}
            '''
        )

        self.assertEqual(resp['data']['tagUpdate']['ok'], False)

    def test_update_tag_failed_name_reason(self):
        resp = self._graphql_helper.query(
            f'''
            mutation tagUpdate{{
                tagUpdate(newTag:{{id:{self._tag_obj.id}, name: ""}}){{
                    errors{{
                        field
                        messages
                    }}
                }}
            }}
            '''
        )
        print
        self.assertEqual(resp['data']['tagUpdate']['errors'][0]['field'], 'name')

    def test_update_tag_name(self):
        resp = self._graphql_helper.query(
            f'''
            mutation tagUpdate{{
                tagUpdate(newTag:{{id:{self._tag_obj.id}, name: "newName"}}){{
                    tag{{
                        name
                    }}
                }}
            }}
            '''
        )
        self.assertEqual(resp['data']['tagUpdate']['tag']['name'], "newName")

    def test_delete_tag(self):
        resp = self._graphql_helper.query(
            f'''
            mutation tagDelete {{
                tagDelete(id: {self._tag_obj.id}) {{
                    ok
                }}
            }}
            '''
        )
        self.assertEqual(resp['data'], {'tagDelete': {'ok': True}})
