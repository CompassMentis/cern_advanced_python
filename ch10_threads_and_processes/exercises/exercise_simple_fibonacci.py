import timeit

# TODO (overview) manually create a producer/worker pattern using multi-processing, to speed up the overall process
#   ... by following the steps below


def fibonacci(n):
    def fib(n):
        if n <= 2:
            return 1
        return fib(n - 2) + fib(n - 1)
    return fib(n)

# TODO: In main(), create a task_queue and a results_queue
#   For the task_queue use multiprocessing.JoinableQueue
#       See https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue
#   For the result queue use multiprocessing.Queue
#       See https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue
#   Warning: Do not use the queue module - this only works with threads

# TODO: Create a worker function which, in an infinite loop
#   - takes a number, n, off the task_queue
#   - calculates the fibonacci number for n
#   - puts a tuple (n, fibonacci(n)) on the results queue
#   - marks the task as done

# TODO: The main code will be the producer, and should do the following:
#   - create the queues (already done, see above)
#   - Put the numbers from 1 .. n (inclusive) on the task queue
#   - Creates NUMBER_OF_WORKERS (constant, start with 4) workers, as separate processes
#       Make sure they are daemon processes
#   - Start the workers
#   - Wait for the task_queue to be done (i.e. join)
#   - Get the results off the result queue, sort them, and print them out as a simple table

# TODO: Run the code, check the results, write down the times, compare this against the starting time

# TODO: Try out different NUMBER_OF_WORKERS - try to find the one which gives you the shortest time


def fibonacci_list(n):
    return [
        (i, fibonacci(i))
        for i in range(1, n + 1)
    ]


def main():
    print(fibonacci_list(40))


print(timeit.timeit('main()', number=1, globals=locals()))
