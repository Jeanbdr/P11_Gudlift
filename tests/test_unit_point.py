def test_reflect_point(client, mock_Clubs, mock_Competitions):
    # This test is a proof that site will make a substraction when places are booked
    competition = mock_Competitions[0]
    club = mock_Clubs[1]
    message = "Points available:"
    response = client.post('/purchasePlaces', data={'competition': competition['name'], 'club':club['name'], 'places': 4})
    assert response.status_code == 200
    assert message in str(response.data)
