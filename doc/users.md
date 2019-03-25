## Sign in

### Table of contents

* [Introduction](#introduction)
* [Interface for signing in](#interface-for-signing-in)
* [Interface for refreshing a token](#interface-for-refreshing-a-token)
* [Interface for verifying a token](#interface-for-verifying-a-token)

### Introduction

One must have an account to get an access to Office manager platform. To create a new account (to sign up), provide the username and password.
They are also used for signing in the system.

When a user is signed up, the can get an access token to start working with Backend. By default, access token is expired in 1 hour.

The access is the [JSON Web Token](https://jwt.io/) (JWT). It contains the following encoded JSON payload.

`{'user_id': <USER_ID>, 'username': <USERNAME>, 'exp': <EXP> }`

* `user_id` is a user id. It accepts integer numbers.
* `username` is a user username.
* `exp` is an expiration date. It accepts integer numbers known as Unix timestamps.

For more information you can see the [Django REST framework JWT Auth](http://getblimp.github.io/django-rest-framework-jwt/) documentation.

### Interface for signing in

Obtains the token.

* **URI:**  `/api-token-auth/`
* **Method:** `POST`
* **Params:**
    * `username=[string]`
    * `password=[string]`
* **Success Response:**
    * **Code:** 200
    * **Content:** `{"token": "<ACCESS_TOKEN>"}`, where `"token"` is a JWT token.
* **Error Response:**
    * **Code:** 400
    * **Content:** `{"non_field_errors":["Error decoding signature."]}`
* **Simple Call:**
    `$ curl -X POST -d "username=some_user&password=secret_password" http://127.0.0.1/api-token-auth/`


### Interface for refreshing a token

To obtain a brand new token with renewed expiration time.

**Pay attention!**
The access token can be refreshed only when it's **non-expired**.

* **URI:**  `/api-token-refresh/`
* **Method:** `POST`
* **Params:**
    * `token=[string]`, where `token` is your existing access JWT token.
* **Success Response:**
    * **Code:** 200
    * **Content:** `{"token": "<ACCESS_TOKEN>"}`
* **Error Response:**
    * **Code:** 400
    * **Content:** `{"non_field_errors":["Signature has expired."]}`
* **Simple Call:**
    `$ curl -X POST -H "Content-Type: application/json" -d '{"token":"<EXISTING_TOKEN>"}' http://localhost:8000/api-token-refresh/`

### Interface for verifying a token

To confirm that JWT is valid.

* **URI:**  `/api-token-verify/`
* **Method:** `POST`
* **Params:**
    * `token=[string]`, where `token` is your existing access JWT token.
* **Success Response:**
    * **Code:** 200
    * **Content:** `{"token": "<ACCESS_TOKEN>"}`
* **Error Response:**
    * **Code:** 400
    * **Content:** `{"non_field_errors":["Signature has expired."]}`
* **Simple Call:**
    `$ curl -X POST -H "Content-Type: application/json" -d '{"token":"<EXISTING_TOKEN>"}' http://localhost:8000/api-token-refresh/`

