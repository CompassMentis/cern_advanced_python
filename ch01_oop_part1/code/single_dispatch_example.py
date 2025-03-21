import functools

@functools.singledispatch
def pretty_print(collection):
    pass

@pretty_print.register(list)
def _(collection):
    print(f'A list with {len(collection)} items')
    print(', '.join(str(element) for element in collection))

@pretty_print.register(dict)
def _(collection):
    print(f'A dictionary with {len(collection)} items')
    for key, value in collection.items():
        print(f'{key}: {value}')

pretty_print([1, 2, 3, 7])
pretty_print(dict(a=10, b=15, c=100))
