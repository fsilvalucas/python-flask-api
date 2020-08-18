import json


# O `client` é a fixture que criamos dentro do arquivo conftest.py
# ela é passada por parâmetro na função e pode ser usada dentro do escopo dela


def test_index_response_200(client):
    # Realiza uma requisição HTTP do tipo get para o endpoint /
    response = client.get('/')

    # Verificamos a assertividade do código de resposta da requisição
    # http. Ela deve ser exatamente igual 200 retornando um True para
    # o teste
    assert response.status_code == 200


def test_home_response_hello(client):
    # Realiza uma requisição HTTP do tipo get para o endpoint /
    response = client.get('/')

    # Utilizamos a função loads do modulo json para retornar um dict
    # para a váriavel data.
    # Precisamos passar por parâmetro para essa função a resposta
    # retornada pelo servidor, através da váriavel response.data
    # e decodificar para utf-8
    data = json.loads(response.data.decode('utf-8'))

    assert data['Hello'] == 'World'
