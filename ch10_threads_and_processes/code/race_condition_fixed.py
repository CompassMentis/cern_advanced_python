import threading

counter = dict(cats=0, dogs=0)
counter_lock = threading.Lock()


def one():
    return 1


def plus_many_cats(number=100_000):
    for _ in range(number):
        with counter_lock:
            counter['cats'] += one()


print('start')
threads = [
    threading.Thread(target=plus_many_cats)
    for _ in range(5)
]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(counter)
# Expected: 5 * 100,000 = 500,000
# Output, Python 3.11:
# Without lock, {'cats': 441062, 'dogs': 0}
# With lock, {'cats': 500000, 'dogs': 0}
