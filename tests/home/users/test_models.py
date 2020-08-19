from mongoengine import (
    BooleanField,
    StringField,
)
from typing import Dict, Union

# Apps

from apps.users.models import User


# Lembre-se que o conftest.py cria uma sessao do flask apenas para testes
# automatizados.

class TestUser:
    def setup_method(self):
        self.data: Dict[str, Union[str, bool]] = {
            'email': 'teste1@teste.com',
            'password': 'teste',
            'active': True,
            'full_name': "teste",
            'cpf_cnpj': '11111111'
        }

        # Instancia do Modelo User
        self.model: User = User(**self.data)

    def test_email_field_exists(self) -> None:
        """
        Verifica se o historico do campo e-mail existe
        """
        assert 'email' in self.model._fields

    def test_email_field_is_requires(self) -> None:
        """
        verifica se o campo email e requerido
        """
        assert self.model._fields['email'].required is True

    def test_email_field_is_unique(self) -> None:
        """
        Verifica se o campo email eh unico
        """
        assert self.model._fields['email'].unique is True

    def test_email_field_is_str(self) -> None:
        """
        verifica se o campo email eh do tipo string
        """
        assert isinstance(self.model._fields['email'], StringField)

    def test_active_field_exists(self) -> None:
        """
        verifica se o campo active existe
        """
        assert 'active' in self.model._fields

    def test_active_field_is_default(self) -> None:
        """
        verifica se o campo active tem default igual a False
        """
        assert self.model._fields['active'].default is False

    def test_active_field_is_bool(self) -> None:
        """
        Verifico se o campo active é booleano
        """
        assert isinstance(self.model._fields['active'], BooleanField)

    def test_full_name_field_exists(self) -> None:
        """
        Verifico se o campo full_name existe
        """
        assert 'full_name' in self.model._fields

    def test_full_name_field_is_str(self) -> None:
        assert isinstance(self.model._fields['full_name'], StringField)

    def test_all_fields_in_model(self) -> None:
        """
        Verifico se todos os campos estão de fato no meu modelo
        """
        fields = [
            'active', 'address', 'cpf_cnpj', 'created', 'email',
            'full_name', 'id', 'password', 'roles'
        ]

        model_keys = [i for i in self.model._fields.keys()]

        fields.sort()
        model_keys.sort()

        assert fields == model_keys
