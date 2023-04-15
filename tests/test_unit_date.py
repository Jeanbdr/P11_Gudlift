from freezegun import freeze_time
import pytest

@pytest.mark.parametrize("email, expected_message, date", 
[("admin@ironman.com","Event done","2099-10-10 10:10:00"),
("admin@ironman.com","Book Places",'2019-01-10 10:00:00')])
def test_date(client, date, email, expected_message):
    with freeze_time(date):
        response = client.post('/showSummary', data={'email': email})
        assert response.status_code == 200
        assert expected_message in str(response.data)
