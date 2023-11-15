"""
Only use this code for learning to mock code for unit testing
Check the Wikimedia REST API documentation before using it for anything else
See https://en.wikipedia.org/api/rest_v1/#/
"""


import requests


def get_response(title):
    base_url = 'https://en.wikipedia.org/api/rest_v1/page/summary/'
    response = requests.get(base_url + title)
    assert response.status_code == 200
    return response


def get_summary(title):
    response = get_response(title)
    json = response.json()
    return json['extract']


if __name__ == '__main__':
    summary = get_summary('CERN')
    print(summary)
