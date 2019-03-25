### Overview 
 The Authentication uses REST API, other features use GraphQL API.
 

## Table of contents

* [Users and Authentication](users.md)
* [Notes for GraphQL](#notes-for-graphql)
* [Library](library.md)


### Notes for GraphQL
 
 The **GraphQL** API endpoint for all requests is `/graphql`
 
#### Authentication
 
 Requests  must be authenticated using a JWT token auth. (See the [auth article](users.md))
 Pass the token in your GraphQL request using the **Authorization** HTTP header with a value `JWT <TOKEN>`
 
 For example: 
 
 `curl -H "Authorization: JWT <YOUR_JWT_TOKEN>"" http://127.0.0.1/graphql/`
 
#### Performing requests with curl

 **GraphQL** request is a standard HTTP POST, with a JSON-encoded body containing a `query` key.
 
 For example:
 
 ```
    curl http://127.0.0.1/graphql/ \
    -H "Authorization: JWT <TOKEN>" \
    -d '{
        "query": "{ books { name } }"
    }'
 ```
  
