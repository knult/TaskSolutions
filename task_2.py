"""
Call https://freegeoip.app/json/ API and perform the following actions:
a) Assert the response code;
b) Parse the response;
c) Assert your latitude and longitude with a 0.01° tolerance (assume you know your actual lat and lon).
"""
import requests
import pytest


apikey = 'YOUR API KEY'
url = "https://freegeoip.app/json/"


@pytest.fixture(scope='module')
def response():
    headers = {'Content-Type': 'application/json', 'apikey': apikey}
    response = requests.request("GET", url, headers=headers)
    return response

@pytest.mark.parametrize('expected_status_code', [200])
def test_status_code(expected_status_code, response):
    assert response.status_code == expected_status_code

@pytest.mark.parametrize('key, value', [
    ('latitude', 43.25),
    ('longitude', 76.89),
    # ('country_code', 'KZ'),
    # ('country_name', 'Kazakhstan'),
    # ('region_code', None),
    # ('region_name', ''),
    # ('city', 'Almaty'),
    # ('zip_code', '050009'),
    # ('time_zone', 'Asia/Almaty'),
    # ('metro_code', 0),
    # ('ip', '8.8.8.8')
])
def test_json(key, value, response):
    parsed_resp = response.json()
    if key in ['latitude', 'longitude']:
        assert round(parsed_resp[key], 2) == value
    else:
        assert parsed_resp[key] == value

