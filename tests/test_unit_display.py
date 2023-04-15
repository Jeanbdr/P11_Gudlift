def test_displayboard(client):
    # This is used to verify if we find the name of a club in our display board
    response = client.get('/pointsBoard')
    message = "<h3>Club points display board </h3>\\n    <h6>brought you by Gudlft</h6>"
    assert message in str(response.data)
    assert response.status_code == 200
    