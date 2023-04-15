def test_booking(client, mock_Clubs, mock_Competitions):
    # Here we test the full process of booking
    club = mock_Clubs[1]
    competition = mock_Competitions[0]

    # First of we log with an existing account
    response = client.post("/showSummary", data={"email":club["email"]}, follow_redirects=True)
    message = f"Welcome, {club['email']}"
    assert response.status_code == 200
    assert message in str(response.data)

    # Then we go to booking page of an event
    response = client.get(f"/book/{competition['name']}/{club['name']}", follow_redirects=True)
    message = "Places available"
    assert message in str(response.data)
    assert response.status_code == 200

    # Finally we book some place
    response = client.post('/purchasePlaces', data={'club':club['name'], 'competition':competition['name'], 'places':1}, follow_redirects=True)
    message = "Great-booking complete!"
    assert message in str(response.data)
    assert response.status_code == 200