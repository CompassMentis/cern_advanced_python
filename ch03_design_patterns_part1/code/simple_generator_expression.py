numbers = [1, 2, 7, 10]

squares = (
    number ** 2
    for number in numbers
)

print(squares)
# <generator object <genexpr> at 0x7f56a4d53370>

print(list(squares))
# [1, 4, 49, 100]
