import time

# Todo: Create a context manager called 'Timed'

# Todo: When entering, it should return the start time
#   hint: time.time()

# Todo: When exiting, it should calculate the duration (end time - start time)
#   And print it out as: Duration ... seconds

class Timed:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        print(f'Duration {duration:0.3f} seconds')


a = 5
b = 4
with Timed():
    a = (a ** 1001234) % 1000
print(a)
