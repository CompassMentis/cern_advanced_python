import threading
import time

resource_a = []
lock_a = threading.Lock()

resource_b = []
lock_b = threading.Lock()

def process_x():
    print('Started x')
    with lock_a:
        print('process x, lock A claimed')
        time.sleep(1)
        print('process x, waiting for lock B')
        with lock_b:
            resource_a.append(1)
            resource_b.append(2)

def process_y():
    print('Started y')
    with lock_b:
        print('process y, lock B claimed')
        time.sleep(1)
        print('process y, waiting for lock A')
        with lock_a:
            resource_a.append(1)
            resource_b.append(2)

threading.Thread(target=process_x).start()
threading.Thread(target=process_y).start()

