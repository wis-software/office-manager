# Library

### Overview

Library is a part of CRM, which is a book location control system. 

The company has a collection of printed books, which every employee can take to read. Information about it should be placed in a holders. Every employee can add a new book to the 'wish list' (offers).


### Table of contents

* [Books](#books)
    * [Introduction](#book-introduction)
    * [Model](#book-model)
    * [Queries](#book-queries)
    * [Mutations](#book-mutations)
* [Holders](#holders)
    * [Introduction](#holder-introduction)
    * [Model](#holder-model)
    * [Queries](#holder-queries)
    * [Mutations](#holder-mutations)
* [Offers](#offers)
    * [Introduction](#offer-introduction)
    * [Model](#offer-model)
    * [Queries](#offer-queries)
    * [Mutations](#offer-mutations)
* [Tags](#tags)
    * [Introduction](#tag-introduction)
    * [Model](#tag-model)
    * [Queries](#tag-queries)
    * [Mutations](#tag-mutations)
* [Authors](#authors)
    * [Introduction](#author-introduction)
    * [Model](#author-model)
    * [Queries](#author-queries)
    * [Mutations](#author-mutations)
* [Publishers](#publishers)
    * [Introduction](#publisher-introduction)
    * [Model](#publisher-model)
    * [Queries](#publisher-queries)
    * [Mutations](#publisher-mutations)
    
## Books

### Book Introduction

**Book** is an entity which is a collection of the company's books.

### Book Model
**Book** contains following information:

| Argument            | Type   | Notes                       |
|---------------------|:------:|-----------------------------|
| `name`              | String |                             |
| `decription`        | Text   |optional                     |
| `publication_number`| Int    |                             |

**Relationships:**

* `tags`
* `specializations`
* `authors`
* `publishers`


### Book Queries

* List of books

        query { 
            books {
                id
                name
            }
        }
    Response:
    
        {
            "data": {
                "books": [
                    {
                        "id": 1,
                        "name": 'Python Coockbook'
                    }
                ]
            }
        }
        
* Get total books count

        query {
           totalBooks 
        }
        
    Response:
    
        {
            "data": {
                "totalBooks": 1
            }
        }
      
### Book Mutations

* Create book
* 
        {
            mutation: bookCreate{
                bookCreate(newBook: {name: "Python Cookbook", author: "David Asher", publisher: "O'relly"}){
                    ok
                    book {
                        name
                        author
                        publisher
                    }
                }
            }
        }
 
        
    Response:

        {
            "data": {
                "bookCreate": {
                    "ok": True,
                    "book": {
                        "name": "Python Cookbook",
                        "author": "David Asher",
                        "publisher": "O'relly"
                    }
                }
            } 
        }

* Update book

        {
            mutation: bookUpdate{
                bookUpdate(newBook:{id: 1, name: "New book name"}){
                    ok
                    book {
                        id
                        name
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "bookUpdate": {
                    "ok": True,
                    "book": {
                        "id": 1,
                        "name": "New book name"
                    }
                }
            }
        }

* Delete book
        
        {
            mutation: bookDelete{
                bookDelete(id: 1){
                    ok
                }
            }
        }
        
    Response:
   
        {
            "data": {
                "bookDelete" : {
                    "ok": True
                }
            }
        }

## Holders

### Holder Introduction

**Holder** is an entity which contains information about taking the book by the employee.

### Holder Model
**Holder** contains following information:

| Argument            | Type     | Notes                       |
|---------------------|:--------:|-----------------------------|
| `employeeId`        | Int      | reference to Employee model |
| `bookId`            | Int      | reference to Book model     |
| `notes`             | String   | optional                    |
| `refunded_at`       | DateTime | the date of refund, optional|

### Holder Queries

* List of holders

        query { 
            holders {
                id
                book {
                    id
                }
                employee {
                    id
                }
            }
        }
    Response:
    
        {
            "data": {
                "holders": [
                    {
                        "id": 1,
                        "book":  {
                            "id": 1
                        }
                        employee: {
                            "id": 1
                        }
                    }
                ]
            }
        }
        
* Get total holders count

        query {
           totalHolders 
        }
        
    Response:
    
        {
            "data": {
                "totalHolders": 1
            }
        }
      
### Holder Mutations

* Create holder

        {
            mutation: holderCreate{
                holderCreate(newHolder: {notes: "Holder notes", employee: 1, book: 1}){
                    ok
                    holder {
                        notes
                        book {
                            id
                        }
                        employee {
                            id
                        }
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "holderCreate": {
                    "ok": True,
                    "holder": {
                        "notes": "Holder notes",
                        "book": {
                            "id": 1,
                        },
                        "employee": {
                            "id": 1,
                        },
                    }
                }
            } 
        }

* Update holder

        {
            mutation: holderUpdate{
                holderUpdate(newHolder:{id: 1, notes: "New notes holder"}){
                    ok
                    holder {
                        id
                        notes
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "holderUpdate": {
                    "ok": True,
                    "holder": {
                        "id": 1,
                        "notes": "New notes holder"
                    }
                }
            }
        }

* Delete holder
        
        {
            mutation: holderDelete{
                holderDelete(id: 1){
                    ok
                }
            }
        }
        
    Response:
   
        {
            "data": {
                "holderDelete" : {
                    "ok": True
                }
            }
        }

## Offers

### Offer Introduction

**Offer** is an entity which contains information about books was added to the 'wish list'.

### Offer Model
**Offer** contains following information:

| Argument            | Type     | Notes                       |
|---------------------|:--------:|-----------------------------|
| `employeeId`        | Int      | reference to Employee model |
| `bookId`            | Int      | reference to Book model     |
| `name`              | String   | optional                    |
| `url`               | String   | optional                    |
| `price`             | String   | default: 0                  |
| `count`             | Int      | default: 1                  |
| `description`       | Text     | optional                    |

### Offer Queries

* List of offers

        query { 
            offers {
                id
                url
            }
        }
    Response:
    
        {
            "data": {
                "offers": [
                    {
                        "id": 1,
                        "url": "http://example-book-url.com"
                    }
                ]
            }
        }
        
* Get total offers count

        query {
           totalOffers 
        }
        
    Response:
    
        {
            "data": {
                "totalOffers": 1
            }
        }
      
### Offer Mutations

* Create offer

        {
            mutation: offerCreate{
                offerCreate(newOffer: {name: "Harry Potter and the philosopher's stone", employee: 1, book: 1}){
                    ok
                    offer {
                        name
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "offerCreate": {
                    "ok": True,
                    "offer": {
                        "name": "Harry Potter and the philosopher's stone",
                    }
                }
            } 
        }

* Update offer

        {
            mutation: offerUpdate{
                offerUpdate(newOffer:{id: 1, name: "Harry Potter and the chamber of secrets"}){
                    ok
                    offer {
                        id
                        name
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "offeerUpdate": {
                    "ok": True,
                    "offer": {
                        "id": 1,
                        "name": "Harry Potter and the chamber of secrets"
                    }
                }
            }
        }

* Delete offer
        
        {
            mutation: offerDelete{
                offerDelete(id: 1){
                    ok
                }
            }
        }
        
    Response:
   
        {
            "data": {
                "offerDelete" : {
                    "ok": True
                }
            }
        }

## Tags

### Tag Introduction

**Tag** is an identifier for the book categorization.

### Tag Model
**Tag** contains following information:

| Argument | Type     |
|----------|:--------:|
| `name`   | String   |

### Tag Queries

* List of tags

        query { 
            offers {
                id
                name
            }
        }
    Response:
    
        {
            "data": {
                "tags": [
                    {
                        "id": 1,
                        "name": "ruby >:>"
                    }
                ]
            }
        }
        
* Get total tags count

        query {
           totalTags 
        }
        
    Response:
    
        {
            "data": {
                "totalTags": 1
            }
        }
      
### Tag Mutations

* Create tag

        {
            mutation: tagCreate{
                tagCreate(newTag: {name: "angular"}){
                    ok
                    tag {
                        name
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "offerCreate": {
                    "ok": True,
                    "tag": {
                        "name": "angular",
                    }
                }
            } 
        }

* Update tag

        {
            mutation: tagUpdate{
                tagUpdate(newTag:{id: 1, name: "backend"}){
                    ok
                    tag {
                        id
                        name
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "offeerUpdate": {
                    "ok": True,
                    "offer": {
                        "id": 1,
                        "name": "backend"
                    }
                }
            }
        }

* Delete tag
        
        {
            mutation: tagDelete{
                tagDelete(id: 1){
                    ok
                }
            }
        }
        
    Response:
   
        {
            "data": {
                "tagDelete" : {
                    "ok": True
                }
            }
        }

## Authors

### Author Introduction

**Author** is an entity that represents the book author.

### Author Model
**Author** contains following information:

| Argument            | Type   | Notes                       |
|---------------------|:------:|-----------------------------|
| `name`              | String |                             |
| `about`             | Text   |optional                     |

### Author Queries

* List of authors

        query { 
            authors {
                id
                name
            }
        }
    Response:
    
        {
            "data": {
                "authors": [
                    {
                        "id": 1,
                        "name": "Joan Rowling"
                    }
                ]
            }
        }

### Author Mutations

* Create author

        {
            mutation: authorCreate{
                authorCreate(newAuthor: {name: "Joan Rowling", about: "Harry Potter's writer"}){
                    ok
                    author {
                        name
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "authorCreate": {
                    "ok": True,
                    "author": {
                        "name": "Joan Rowling",
                    }
                }
            } 
        }

* Update author

        {
            mutation: authorUpdate{
                authorUpdate(newAuthor:{id: 1, name: "Stephen King"}){
                    ok
                    author {
                        id
                        name
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "authorUpdate": {
                    "ok": True,
                    "author": {
                        "id": 1,
                        "name": "Stephen King"
                    }
                }
            }
        }

* Delete author
        
        {
            mutation: authorDelete{
                authorDelete(id: 1){
                    ok
                }
            }
        }
        
    Response:
   
        {
            "data": {
                "authorDelete" : {
                    "ok": True
                }
            }
        }


## Publishers

### Publisher Introduction

**Publisher** is an entity that represents the book publisher.

### Publisher Model
**Publisher** contains following information:

| Argument            | Type   | Notes   |
|---------------------|:------:|---------|
| `title`             | String |         |
| `decription`        | Text   |optional |

### Publisher Queries

* List of publishers

        query { 
            publishers {
                id
                title
            }
        }
    Response:
    
        {
            "data": {
                "publishers": [
                    {
                        "id": 1,
                        "title": "Bloomsbury"
                    }
                ]
            }
        }
        
      
### Publisher Mutations

* Create publisher

        {
            mutation: publisherCreate{
                publisherCreate(newPublisher: {title: "O'relly"}){
                    ok
                    publisher {
                        title
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "publisherCreate": {
                    "ok": True,
                    "publisher": {
                        "title": "O'relly",
                    }
                }
            } 
        }

* Update publisher

        {
            mutation: publisherUpdate{
                publisherUpdate(newPublisher:{id: 1, title: "Macmillan"}){
                    ok
                    publisher {
                        id
                        title
                    }
                }
            }
        }
        
    Response:
    
        {
            "data": {
                "offeerUpdate": {
                    "ok": True,
                    "publisher": {
                        "id": 1,
                        "title": "Macmillan"
                    }
                }
            }
        }

* Delete publisher
        
        {
            mutation: publisherDelete{
                publisherDelete(id: 1){
                    ok
                }
            }
        }
        
    Response:
   
        {
            "data": {
                "publisherDelete" : {
                    "ok": True
                }
            }
        }
