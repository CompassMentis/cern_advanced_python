import timeit


code = """
def add(a,b):
    return a + b
"""
print(
    timeit.timeit(stmt=code, number=10000)
)
# Output:
# 0.0006105689972173423
