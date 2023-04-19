import pytest

@pytest.mark.parametrize("competition_index, club_index, places, expected_message",
[(0, 2, 1, 'Great-booking complete!'),
(0, 1, 75, 'You can&#39;t get more places than your number of available points')])
def test_purchase(client, competition_index, club_index, places, expected_message, mock_Competitions, mock_Clubs):
    # This test is a proof that booking more or less places than you get return an expected message
    competition = mock_Competitions[competition_index]
    club = mock_Clubs[club_index]
    response = client.post('/purchasePlaces', data={'competition':competition["name"], "club":club["name"], "places": places})
    assert response.status_code == 200
    assert expected_message in str(response.data)