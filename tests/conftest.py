import pytest
import server


@pytest.fixture
def client(monkeypatch, mock_Clubs, mock_Competitions):
    monkeypatch.setattr(server, "clubs", mock_Clubs)
    monkeypatch.setattr(server, "competitions", mock_Competitions)
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def mock_Clubs():
    return [
        {"name": "Simply Unlift", "email": "sam@simplylift.co", "points": "75"},
        {"name": "Iron Man", "email": "admin@ironman.com", "points": "25"},
        {"name": "Squat Boyz", "email": "admin@squat.com", "points": "30"},
    ]


@pytest.fixture
def mock_Competitions():
    return [
        {
            "name": "Springfield Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25",
        },
        {
            "name": "Fallout Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13",
        },
    ]
