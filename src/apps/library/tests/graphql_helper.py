import json

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


class GraphQLHelper(TestCase):
    """
    Would be used for testing GraphQL queries
    """

    def __init__(self, *args, **kwargs):
        super(GraphQLHelper, self).__init__(*args, **kwargs)
        self._user = {
            'username': 'test.user',
            'password': 'secret',
            'email': 'test.user@domain.com',
        }
        User.objects.create_user(**self._user)

        self._client = Client()

    def query(self, query: str):
        """
        :param query: GraphQL query to run
        :return: dict response from /graphql endpoint. The response has a 'data' key.
                 It will have the 'error' key if any error happened.
        """

        auth = self._client.post('/api-token-auth/', data=json.dumps(self._user),
                                content_type='application/json')

        self.fake_header = b'JWT ' + json.loads(auth.content)['token'].encode()

        resp = self._client.post('/graphql/', json.dumps({'query': query}),
                                 HTTP_AUTHORIZATION=self.fake_header,
                                 content_type='application/json')
        json_resp = json.loads((resp.content.decode()))

        return json_resp

    def assertResponseNoErrors(self, resp: dict, expected: dict):
        """
        Assert that the resp (as returned from query) has the data from expected
        """
        self.assertNotIn('errors', resp, 'Response had errors')
        self.assertEqual(resp, expected, 'Response has correct data')
