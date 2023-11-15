import pathlib
import time
import timeit


def get_value_from_api(id):
    lines = pathlib.Path('../data/api_data.txt').read_text().split('\n')
    time.sleep(0.02)
    return int(lines[id])

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
    total = 0
    for i in range(100):
        value = get_value_from_api(i)
        total += value
    print(total)


print(timeit.timeit('main()', number=1, globals=locals()))

# Expected output:
# 53098958
# (plus the time from timeit, e.g. 2.0495059989989386)
