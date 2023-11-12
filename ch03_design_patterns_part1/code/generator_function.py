def squares(number_of_squares):
    for number in range(1, number_of_squares + 1):
        yield number ** 2


print(squares(4))
# <generator object squares at 0x7f3fe4e37ae0>

for number in squares(5):
    print(number)

# Output
# 1
# 4
# 9
# 16
# 25
