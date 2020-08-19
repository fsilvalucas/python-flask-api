from flask_restful import Api, Resource

# App
from apps.users.resource import SignUp


class Index(Resource):

    def get(self):
        return {'Hello': 'World'}


api = Api()


def configure_api(app):
    api.add_resource(Index, '/')
    api.add_resource(SignUp, '/users')

    api.init_app(app)
