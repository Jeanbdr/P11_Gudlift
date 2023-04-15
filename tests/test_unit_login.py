import pytest

@pytest.mark.parametrize("email, expected_message", 
[("exemple@email.com","Sorry the email wasn&#39;t found"),
('admin@ironman.com',"Points available")])
def test_email(client, email, expected_message):
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    assert expected_message in str(response.data)

def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302