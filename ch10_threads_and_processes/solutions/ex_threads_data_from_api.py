import pathlib
import time
import timeit
import threading


class GetValueFromAPI(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.result = None

    def run(self):
        lines = pathlib.Path('../data/api_data.txt').read_text().split('\n')
        time.sleep(0.02)
        self.result = int(lines[self.id])

# TODO: Run the code and write down the output, including the duration from timeit

# TODO: Create 100 threads - as subclasses for threading.Thread
#   all threads run get_value_from_api
#   each threads calculates it for one of the numbers 0 .. 99
#   and stores the result in a 'value' attribute

# TODO: start the threads, wait until they are all done

# TODO: sum up all the 'value' attributes and print out the total
#   Compare this against the expected value

# TODO: Compare the new time against the old time


def main():
    threads = [
        GetValueFromAPI(id)
        for id in range(100)
    ]
    for thread in threads:
        thread.start()

    total = 0
    for thread in threads:
        thread.join()
        total += thread.result

    print(total)


print(timeit.timeit('main()', number=1, globals=locals()))

# Expected output:
# 53098958
# (plus the time from timeit, e.g. 2.0495059989989386)
# Time, from time it, is now 0.038842035000925534
