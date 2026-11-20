# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test a RESTful API using FastAPI, Pydantic models, HTTP methods, and in-memory data storage.

## 📝 Tasks

### 🛠️ Create the Book Data Model

#### Description
Start with the starter code and define a Pydantic model for a book.

#### Requirements
Completed program should:

- Define a `Book` model with `title`, `author`, and `publication_year` fields
- Require the `title` and `author` fields to contain at least one character
- Require `publication_year` to be an integer between 1000 and 2100
- Add a unique integer `id` field to books returned by API endpoints

### 🛠️ Implement REST Endpoints

#### Description
Create API endpoints that manage a collection of books stored in memory.

#### Requirements
Completed program should:

- Return all books from `GET /books`
- Return a book by ID from `GET /books/{book_id}`
- Create a book from `POST /books` and return the created book
- Return HTTP 404 with a clear detail message when an ID does not exist
- Return HTTP 201 for successful book creation

### 🛠️ Add Update and Delete Operations

#### Description
Complete the API by allowing students to update and remove books.

#### Requirements
Completed program should:

- Replace an existing book from `PUT /books/{book_id}`
- Delete an existing book from `DELETE /books/{book_id}`
- Return HTTP 404 when update or delete targets an unknown ID
- Return a 204 No Content response after successful deletion

### 🛠️ Test the API

#### Description
Run the application and verify each endpoint using FastAPI's interactive documentation or HTTP client.

#### Requirements
Completed program should:

- Start successfully with `uvicorn starter-code:app --reload`
- Include working examples in Swagger UI at `/docs`
- Demonstrate creating, reading, updating, and deleting at least one book
- Return validation errors for invalid book data
