def test_redeem_work(client, mock_Clubs, mock_Competitions):
    # This test is a proof that booking less (or =) places than you get as a club work (here 1 < 4)
    competition = mock_Competitions[0]
    club = mock_Clubs[2]
    message = 'Great-booking complete!'
    response = client.post('/purchasePlaces', data={'competition':competition["name"], "club":club["name"], "places": 1})
    assert response.status_code == 200
    assert message in str(response.data)

def test_redeem_more_error(client, mock_Clubs, mock_Competitions):
    # This test is a proof that booking more places than you get as a club return an error (here 75 > 4)
    competition = mock_Competitions[0]
    club = mock_Clubs[1]
    message = 'You can&#39;t get more places than your number of available points'
    response = client.post('/purchasePlaces', data={'competition':competition["name"], "club":club["name"], "places": 75})
    assert response.status_code == 200
    assert message in str(response.data)