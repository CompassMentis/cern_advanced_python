import timeit
import multiprocessing

NUMBER_OF_WORKERS = 7

# TODO (overview) manually create a producer/worker pattern using multi-processing, to speed up the overall process
#   ... by following the steps below




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

def fibonacci(n):
    def fib(n):
        if n <= 2:
            return 1
        return fib(n - 2) + fib(n - 1)
    return fib(n)


def worker(task_queue, results_queue):
    while True:
        try:
            number = task_queue.get()
            result = fibonacci(number)
            results_queue.put((number, result))
        finally:
            task_queue.task_done()


def main():
    task_queue = multiprocessing.JoinableQueue()
    results_queue = multiprocessing.Queue()

    for i in range(1, 41):
        task_queue.put(i)

    workers = [
        multiprocessing.Process(target=worker, args=(task_queue, results_queue), daemon=True)
        for _ in range(NUMBER_OF_WORKERS)
    ]

    for w in workers:
        w.start()

    task_queue.join()
    results = []
    while not results_queue.empty():
        results.append(results_queue.get())
    results.sort()

    print(results)


print(timeit.timeit('main()', number=1, globals=locals()))
# Time before using multi-processing: 12.773694906998571
# Times with multi-processing:
#   4 workers: 6.551972387000205
#   8 workers: 8.665901794000092
#   2 workers: 8.156776376999915
#   6 workers: 6.009627409001041
#   5 workers: 6.105925838000985
#   7 workers: 6.050480552999943
