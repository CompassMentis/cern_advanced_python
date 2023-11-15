from unittest import mock
import pytest

# Todo: import get_summary from wikipedia_extracts.py
from wikipedia_extracts import get_summary

# Todo: Write the following (pytest) tests for get_summary:
#   For each test, mock out get_response - do not make actual requests to Wikipedia


# Todo:
#   Test 1: When response.json() is a dictionary, get_summary returns the value for key 'extract'
def test_get_summary_returns_extract():
    expected = 'Summary here please'
    with mock.patch('wikipedia_extracts.get_response', new_callable=mock.Mock()) as mock_get_response:
        json_mock = mock.Mock()
        mock_get_response.return_value = json_mock
        json_mock.json.return_value = {'extract': expected}
        assert get_summary('a') == expected


# Todo:
#   Test 2: When response.json() is a dictionary, and 'extract' is not one of its keys, get_summary raises KeyError
def test_get_summary_needs_extract_as_key():
    with mock.patch('wikipedia_extracts.get_response', new_callable=mock.Mock()) as mock_get_response:
        json_mock = mock.Mock()
        mock_get_response.return_value = json_mock
        json_mock.json.return_value = {}
        with pytest.raises(KeyError):
            get_summary('a')
