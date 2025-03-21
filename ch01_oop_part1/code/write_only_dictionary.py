class WriteOnlyDictionary:
    def __init__(self):
        self._values = {}

    def __getitem__(self, item):
        return self._values[item]

    def __setitem__(self, key, value):
        if key in self._values:
            raise KeyError(f'Key "{key}" already exists')
        self._values[key] = value


demo = WriteOnlyDictionary()
demo['city'] = 'Birmingham'
demo['address'] = '22 High street'
print(demo['city'])
# Birmingham

demo['city'] = 'Manchester'
# KeyError: 'Key "city" already exists'
