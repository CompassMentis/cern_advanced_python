import threading

counter = dict(cats=0, dogs=0)


def one():
    return 1


def plus_many_cats(number=100_000):
    for _ in range(number):
        counter['cats'] += one()
        # counter['cats'] += 1


print('start')
threads = [
    threading.Thread(target=plus_many_cats)
    for _ in range(50)
]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(counter)

# Expected: 5 * 100,000 = 500,000
# Output for counter['cats'] += 1
    # Python 3.9 and earlier, {'cats': 4116481, 'dogs': 0}
    # Python 3.10 and later, {'cats': 5000000, 'dogs': 0}
# Output for counter['cats'] += one()
    # Python 3.8 .. 3.12, {'cats': 3224187, 'dogs': 0}
