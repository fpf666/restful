from flask_restful import Api

from App.apis import Cat

api = Api()

api.add_resource(Cat,'/cat/')


def init_api(app):
    api.init_app(app=app)