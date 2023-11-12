class APIConnector:
    def __init__(self, url):
        self.url = url

    def __enter__(self):
        print('Logging into to the API service')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Logging out of the API service')
        ...

    def get(self, item_id):
        print(f'Getting data for {item_id}')
        return f'Information about {item_id}'


with APIConnector('https://api.some_website.com') as api_connector:
    data = api_connector.get(5)

print(data)

# Output:
# Logging into to the API service
# Getting data for 5
# Logging out of the API service
# Information about 5
