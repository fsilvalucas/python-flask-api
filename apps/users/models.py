from datetime import datetime
from mongoengine import (
    BooleanField,
    DateTimeField,
    DictField,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    URLField
)
from typing import Dict, Union, List

from apps.db import db


class Roles(EmbeddedDocument):
    """
    Roles Permission
    """
    admin: BooleanField = BooleanField(default=False)


class UserMixin(db.Document):
    """
    Default implementation for User Fields
    """
    meta: Dict[str, Union[bool, List[str]]] = {
        'abstract': True,
        'ordering': ['email']
    }

    email: EmailField = EmailField(required=True, unique=True)
    password: StringField = StringField(required=True)
    roles: EmbeddedDocumentField = EmbeddedDocumentField(Roles, default=Roles)
    created: DateTimeField = DateTimeField(default=datetime.now)
    active: BooleanField = BooleanField(default=False)

    def is_activate(self) -> BooleanField:
        return self.active

    def is_admin(self) -> BooleanField:
        return self.roles.admin


class Address(EmbeddedDocument):
    """
    Default implementation for address fields
    """
    meta = {
        'ordering': ['zip_code']
    }
    zip_code = StringField(default='')
    address = StringField(default='')
    number = StringField(default='')
    complement = StringField(default='')
    neughborhood = StringField(default='')
    city = StringField(default='')
    city_id = StringField(default='')
    state = StringField(default='')
    country = StringField(default='BRA')


class User(UserMixin):
    """
    Users
    """
    meta = {'collection': 'users'}

    full_name = StringField(required=True)
    cpf_cnpj = StringField(default='')
    address = EmbeddedDocumentField(Address, default=Address)
