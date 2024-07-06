from flask_restful import Resource, reqparse
from models import db, Todo

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help="Title cannot be blank!")
parser.add_argument('content', type=str, required=True, help="Content cannot be blank!")

class TodoListResource(Resource):
    def get(self):
        todos = Todo.query.all()
        return [{'id': todo.id, 'title': todo.title, 'content': todo.content} for todo in todos], 200

    def post(self):
        args = parser.parse_args()
        todo = Todo(title=args['title'], content=args['content'])
        db.session.add(todo)
        db.session.commit()
        return {'id': todo.id, 'title': todo.title, 'content': todo.content}, 201
    
class TodoResource(Resource):
    def get(self, todo_id):
        todo = Todo.query.get_or_404(todo_id)
        return {'id': todo.id, 'title': todo.title, 'content': todo.content}, 200

    def put(self, todo_id):
        args = parser.parse_args()
        todo = Todo.query.get_or_404(todo_id)
        todo.title = args['title']
        todo.content = args['content']
        db.session.commit()
        return {'id': todo.id, 'title': todo.title, 'content': todo.content}, 200

    def delete(self, todo_id):
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return '', 204