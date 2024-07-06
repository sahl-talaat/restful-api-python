from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import Config
from models import db
from resources import TodoListResource, TodoResource

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)
api.add_resource(TodoListResource, '/api/v1/todos')
api.add_resource(TodoResource, '/api/v1/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True, port=int(Config.SERVER_PORT))


