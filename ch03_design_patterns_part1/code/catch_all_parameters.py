def show_arguments(*args, **kwargs):
    print(type(args))    # <class 'tuple'>
    print(args)          # (5, 10)

    print(type(kwargs))  # <class 'dict'>
    print(kwargs)        # {'name': 'Sam', 'age': 25}


show_arguments(5, 10, name='Sam', age=25)
