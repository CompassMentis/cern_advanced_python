import dis


def plus_plus_two(a, b):
    result = a + b
    result += 2
    return result


dis.dis(plus_plus_two)

# Output
#   4           0 RESUME                   0
#
#   5           2 LOAD_FAST                0 (a)
#               4 LOAD_FAST                1 (b)
#               6 BINARY_OP                0 (+)
#              10 STORE_FAST               2 (result)
#
#   6          12 LOAD_FAST                2 (result)
#              14 LOAD_CONST               1 (2)
#              16 BINARY_OP               13 (+=)
#              20 STORE_FAST               2 (result)
#
#   7          22 LOAD_FAST                2 (result)
#              24 RETURN_VALUE
