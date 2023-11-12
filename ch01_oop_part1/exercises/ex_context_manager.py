import time

# Todo: Create a context manager called 'Timed'

# Todo: When entering, it should return the start time
#   hint: time.time()

# Todo: When exiting, it should calculate the duration (end time - start time)
#   And print it out as: Duration ... seconds

a = 5
b = 4
with Timed():
    a = (a ** 1001234) % 1000
print(a)

# Expected output:
# Duration 0.090 seconds
# 625
# Note: Your duration will be different
