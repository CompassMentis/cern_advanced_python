from unittest import mock
import requests


class Gutendex:
    def get_data(self):
        response = requests.get('http://gutendex.com/books')
        return response.json()

    def number_of_books(self):
        """
        Number of books at Project Gutenberg
        usage: print(Gutendex().number_of_books())
        """
        return self.get_data()['count']


def test_number_of_books():
    gutendex = Gutendex()
    with mock.patch.object(Gutendex, 'get_data', new=mock.Mock()) as mock_get_data:
        mock_get_data.return_value = {'count': 5}
        assert gutendex.number_of_books() == 5

# Output:
# 1 passed in 0.05s
