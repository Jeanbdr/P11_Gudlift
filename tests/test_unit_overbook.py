def test_overbook_alert(client, mock_Clubs, mock_Competitions):
    # Here we check if the site return an alert if we overbook (13 > 12)
    competition = mock_Competitions[0]
    club = mock_Clubs[0]
    message = "You&#39;re not allow to get more than 12 places"
    response = client.post('/purchasePlaces', data={'competition':competition['name'], 'club':club['name'], 'places':13})
    assert response.status_code == 200
    assert message in str(response.data)

def test_book_negative(client, mock_Clubs, mock_Competitions):
    # Here we check if the site return an alert if we underbook (0 > -1)
    competition = mock_Competitions[0]
    club = mock_Clubs[1]
    message = "You can&#39;t put a negative value"
    response = client.post('/purchasePlaces', data={'competition':competition['name'], 'club':club['name'], 'places':-1})
    assert response.status_code == 200
    assert message in str(response.data)

def test_cant_overbook(client, mock_Clubs, mock_Competitions):
    # Here we check if the site return a message if the booking is fine (2 < 12)
    competition = mock_Competitions[0]
    club = mock_Clubs[1]
    message = "Great-booking complete!"
    response = client.post('/purchasePlaces', data={'competition':competition['name'], 'club':club['name'], 'places':2})
    assert response.status_code == 200
    assert message in str(response.data)