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


def mock_get_data():
    return {'count': 5}


def test_number_of_books():
    gutendex = Gutendex()
    gutendex.get_data = mock_get_data
    assert gutendex.number_of_books() == 5

# Output:
# 1 passed in 0.10s
