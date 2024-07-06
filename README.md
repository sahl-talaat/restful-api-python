Overview
The Todo application is a simple RESTful API built using the Flask framework. It allows users to manage their daily tasks by performing basic CRUD (Create, Read, Update, Delete) operations on todo items. Each todo item consists of a title and content, which can be managed through the API endpoints.

Features
1. Create a Todo: Users can create new todo items by providing a title and content.
2. Read Todos: Users can fetch a list of all todo items or retrieve a specific todo item by its ID.
3. Update a Todo: Users can update the title and content of an existing todo item.
4. Delete a Todo: Users can delete a specific todo item by its ID.

Technologies Used
1. Flask: A lightweight WSGI web application framework in Python used to build the API.
2. Flask-RESTful: An extension for Flask that adds support for quickly building REST APIs.
3. Flask-SQLAlchemy: An extension for Flask that adds support for SQLAlchemy, a SQL toolkit and Object-Relational Mapping (ORM) library for Python.
4. Flask-Migrate: An extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
5. python-dotenv: A Python library that allows you to load environment variables from a .env file.

handlers
GET http://localhost:5000/api/v1/todos
POST http://localhost:5000/api/v1/todos
GET http://localhost:5000/api/v1/todos/todo_id
PUT http://localhost:5000/api/v1/todos/todo_id
DELETE http://localhost:5000/api/v1/todos/todo_id# restful-api-python
