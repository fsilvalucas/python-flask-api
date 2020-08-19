from flask import request

from flask_restful import Resource
from bcrypt import gensalt, hashpw
from mongoengine.errors import NotUniqueError, ValidationError

# Apps
from apps.response import (
    resp_already_exists,
    resp_exception,
    resp_data_invalid,
    resp_ok
)
from apps.messages import (
    MSG_NO_DATA,
    MSG_PASSWORD_DIDNT_MATCH,
    MSG_INVALID_DATA,
    MSG_RESOURCE_CREATED
)

# Local
from .models import User
from .schemas import UserRegistrationSchema, UserSchema
from .utils import check_password_in_signup


class SignUp(Resource):
    def post(self, *args, **kwargs):
        # Inicializa todas as variaveis utilizadas
        req_data = request.get_json() or None
        data, errors, result = None, None, None
        password, confirm_password = None, None
        schema = UserRegistrationSchema()

        if req_data is None:
            return resp_data_invalid('Users', {}, msg=MSG_NO_DATA)

        password = req_data.get('password', None)
        confirm_password = req_data.pop('confirm_password', None)

        # Verificacao da senha e confirmacao de senha
        if not check_password_in_signup(password, confirm_password):
            errors = {'password': MSG_PASSWORD_DIDNT_MATCH}
            return resp_data_invalid('Users', errors)

        # Desserializacao dos dados pelo UserregistratioSchema
        try:
            data = schema.load(req_data)
        # Se hover erros retorna resposta invalida
        except ValidationError as err:
            print(err.message)
            return resp_data_invalid('Users', errors=err.message)

        hashed = hashpw(password.encode('utf-8'), gensalt(12))

        # Salvar o modelo de usuario com a senha criptografada e o email
        # em lowercase. Qualquer erro eh retornado uma resposta de erro json
        # ao inves de levantar uma exception no servidor
        try:
            data['password'] = hashed
            data['email'] = data['email'].lower()
            model = User(**data)
            model.save()
        except NotUniqueError:
            return resp_already_exists('Users', 'fornecedor')
        except ValidationError as e:
            return resp_exception(resource='Users', description=str(e), msg=MSG_INVALID_DATA)
        except Exception as e:
            return resp_exception('Users', description=str(e))

        # dump dos dados de acordo com o modelo salvo
        schema = UserSchema()
        result = schema.dump(model)

        return resp_ok('Users', MSG_RESOURCE_CREATED.format('Usuário'), data=result)
