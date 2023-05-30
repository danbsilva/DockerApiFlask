
def test_login_success(client):
    """
    Verifico se o campo uuid existe
    """
    payload = {
        "email":"danilloaugustobsilva@hormail.com",
        "password":"jhkjhk"
    }
    response = client.post('/auth/login', json=payload)
    print(response)
    assert response.status_code == 200


def test_login_unauthorized(client):
    """
    Verifico se o campo uuid existe
    """
    payload = {
        "email":"danilloaugustobsilva@hormail.com",
        "password":"jhkjhk1"
    }
    response = client.post('/auth/login', json=payload)
    print(response)
    assert response.status_code == 401


def test_email_invalid(client):
    """
    Verifico se o campo uuid existe
    """
    payload = {
        "email":"danilloaugustobsilva",
        "password":"jhkjhk1"
    }
    response = client.post('/auth/login', json=payload)
    print(response)
    assert 'The email address is not valid' in response.json['message']['email']


def test_email_domain_name_not_exists(client):
    """
    Verifico se o campo uuid existe
    """
    payload = {
        "email":"danilloaugustobsilva@homail.om",
        "password":"jhkjhk1"
    }
    response = client.post('/auth/login', json=payload)
    print(response)
    assert 'The domain name' in response.json['message']['email']