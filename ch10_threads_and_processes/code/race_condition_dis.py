import dis


def plus_one():
    global a
    a += 1


dis.dis(plus_one)
# Output:
#   4           0 RESUME                   0
#
#   6           2 LOAD_GLOBAL              0 (a)
#              14 LOAD_CONST               1 (1)
#              16 BINARY_OP               13 (+=)
#              20 STORE_GLOBAL             0 (a)
#              22 LOAD_CONST               0 (None)
#              24 RETURN_VALUE
