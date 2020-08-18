from os.path import dirname, isfile, join
import pytest
from dotenv import load_dotenv

_ENV_FILE = join(dirname(__file__), '../.env')

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

# Cria uma fixture que será utilizada no escopo sessão
# ou seja a cada execução do comando pytest
@pytest.fixture(scope='session')
def client():
    from apps import create_app
    flask_app = create_app('testing')

    testing_client = flask_app.test_client()

    # Antes de criar os testes, eh criado um contexto da aplicacao
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # onde o teste ocorre

    # Remove o contesto ao terminar os teste
    ctx.pop()


@pytest.fixture(scope='function')
def mongo(request, client):
    def fin():
        print('\n[teardown] disconnect from db')

    fin()
