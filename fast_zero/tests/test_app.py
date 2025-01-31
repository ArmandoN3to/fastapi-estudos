from fastapi.testclient import TestClient
from fast_zero.app import app
from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client =TestClient(app)  #arrange(organizaçao)

    response = client.get('/') #Act (açao)

    assert response.status_code == HTTPStatus.OK  #ASSERT (garantindo)
    assert response.text =="""<h1>Olá Mundo!<h1>"""   