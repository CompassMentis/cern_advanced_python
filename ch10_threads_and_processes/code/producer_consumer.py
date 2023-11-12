import time
import random
import threading
import queue


def worker(job_queue, results_queue):
    def process_number(number):
        time.sleep(random.random() / 100)
        return number ** 2

    while True:
        number = job_queue.get()
        try:
            result = process_number(number)
            results_queue.put(result)
        finally:
            job_queue.task_done()

### (column break)

start_time = time.time()
job_queue = queue.Queue()
results_queue = queue.Queue()

for number in range(1000):
    job_queue.put(number)

for _ in range(1000):
    threading.Thread(
        target=worker,
        args=(job_queue, results_queue),
        daemon=True
    ).start()

job_queue.join()
total = 0
while not results_queue.empty():
    total += results_queue.get()
print(total)
print(f'Duration: {time.time()-start_time}')

# 1 worker: Duration: 5.103460073471069
# 10 workers: Duration: 0.4994957447052002
# 100 workers: Duration: 0.06876993179321289
# 1000 workers: Duration: 0.09173750877380371
