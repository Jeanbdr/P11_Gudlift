import server
from unittest.mock import patch


def test_load_club(mock_Clubs):
    # Here we check if the mocked data in club is the one use by loadclub func.
    with patch("server.loadClubs", return_value=mock_Clubs):
        expected_result = mock_Clubs
        assert expected_result == server.loadClubs()


def test_load_comp(mock_Competitions):
    # Here we check if the mocked data in competitions is the one use by loadcompetitons func.
    with patch("server.loadCompetitions", return_value=mock_Competitions):
        expected_result = [
            {
                "name": "Springfield Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25",
            },
            {   "name": "Fallout Classic", 
                "date": "2020-10-22 13:30:00", 
                "numberOfPlaces": "13"},
        ]
        assert expected_result == server.loadCompetitions()
