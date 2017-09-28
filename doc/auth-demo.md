Authentication works through [Django REST framework JWT](http://getblimp.github.io/django-rest-framework-jwt/#additional-settings).

Let's try it! I'll use curl and will show an example
like one in the documentation. I'll use curl, but you could use your favorite
software, like **Postman** or **HTTPIE**.

**Authentication**.

Let's create some user in Django.
I used `python3 manage.py createsuperuser` with these credentials:
`some_kind_of_serious_user` as the username and `some_kind_of_serious_password`
as the password. Then it's possible to make a `curl` request to authenticate.

    ~: curl -X POST -d "username=some_kind_of_serious_user&password=some_kind_of_serious_password" http://127.0.0.1/api-token-auth/

    {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNvbWVfa2luZF9vZl9zZXJpb3VzX3VzZXIiLCJleHAiOjE1MDY1ODkyNzMsImVtYWlsIjoiIn0.6ZeHICXWN_r72M_GYvuOHAGfhh2GaEQRGiRg595AymA"}%

Now, as you see, your token is located in the token field.
As you might already know, it's easy to divide, by dots character, and read.

**Token verification**

    ~: curl -X POST -H "Content-Type: application/json" -d  '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNvbWVfa2luZF9vZl9zZXJpb3VzX3VzZXIiLCJleHAiOjE1MDY1OTAzMjAsImVtYWlsIjoiIn0.AZn5880pmIabQ63YKJGdOAs0ZGlBySvDy-1TS80pZfY"}' http://127.0.0.1/api-token-verify/

    {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNvbWVfa2luZF9vZl9zZXJpb3VzX3VzZXIiLCJleHAiOjE1MDY1OTAzMjAsImVtYWlsIjoiIn0.AZn5880pmIabQ63YKJGdOAs0ZGlBySvDy-1TS80pZfY"}

If token is correct, it will be returned.

If it will expire, you will see a message like this one:

    {"non_field_errors":["Signature has expired."]}

Otherwise, it might look like this, if the signature looks wrong:

    {"non_field_errors":["Error decoding signature."]}

**Refreshing tokens**

Tokens could be refreshed, so old token will continue working later.

    ~: curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNvbWVfa2luZF9vZl9zZXJpb3VzX3VzZXIiLCJleHAiOjE1MDY1OTQ4ODIsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE1MDY1OTEyODJ9.GhRwE3Dh69U5Sb0QbrI8hg6MGl5qiOj3ki4Iqar57iY"}' http://127.0.0.1/api-token-refresh/

    {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNvbWVfa2luZF9vZl9zZXJpb3VzX3VzZXIiLCJleHAiOjE1MDY1OTQ5MTAsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE1MDY1OTEyODJ9.4eRtxRE4p31FcXYMcchskBjRJSDfAXnvkNw8eUPrPM4"}
