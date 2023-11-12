def plus_one(x):
    return x + 1


def plus_five(x):
    return x + 5


print(plus_one(5))  # 6

plus_one = plus_five
print(plus_one(5))  # 10

print(plus_one.__name__)  # plus_five
print(plus_one is plus_five)  # True
