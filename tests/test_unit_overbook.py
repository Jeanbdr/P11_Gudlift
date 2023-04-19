import pytest

@pytest.mark.parametrize("competition_index, club_index, places, expected_message",
[(0, 0, 13, "You&#39;re not allow to get more than 12 places"),
(0, 1, -1, "You can&#39;t put a negative value"),
(0, 1, 2, "Great-booking complete!")])
def test_booking(client, competition_index, club_index, places, expected_message, mock_Competitions, mock_Clubs):
    # This test is a proof that if we overbook, underbook or book an expected message is returned in consequences
    competition = mock_Competitions[competition_index]
    club = mock_Clubs[club_index]
    response = client.post('/purchasePlaces', data={'competition':competition['name'], 'club':club['name'], 'places':places})
    assert response.status_code == 200
    assert expected_message in str(response.data)