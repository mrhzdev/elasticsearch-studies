# Basics of Elasticsearch

## Data Structure

1. **INDEX** - in elastic it is a set of documents, making a parallel with RDB's systens, it is like a *database*.

2. **TYPE** - yet in the same parallel used above, types in elastic it is like a *table*.

3. **DOCUMENT** - it is a register in elastic, lika a *row* in SQL systems.

## Request

The Elasticsearch uses RESTful architecture to abstract interaction with Apache Lucene, who is the responsible to manage all the data.

#### The HTTP Verbs:

- `POST` - This verb is used to **CREATE** a new document, but if an `ID` is passed as a param to request, the document will be created with the specified `ID`, if document already exist, it'll be **UPDATED**. The data of documents is 

- `GET` - This verb is used to **RETRIEVE** informations from server, if `ID` is passed to request, it will return just one document.

- `PUT` - It's the verb used to **UPDATE** a document. The `ID` parameter is **REQUIRED** 

- `DELETE` - This verb **DELETE** a document specified with the `ID` parameter passed. But it must be used carefully, because it allow you to **DELETE** your index, and all of your data in that index.
