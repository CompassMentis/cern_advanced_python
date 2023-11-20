import itertools
import threading
import string
import time
import random

import PySimpleGUI


def monitor(control, data):
    for item in itertools.cycle(data):
        control.update(value=item)
        time.sleep(2 * random.random())


controls = [
    PySimpleGUI.Text(''),
    PySimpleGUI.Text(''),
]

layout = [
    controls,
    [PySimpleGUI.Button('Done')]
]

window = PySimpleGUI.Window('Some title', layout, finalize=True)

threads = [
    threading.Thread(target=monitor, args=(controls[0], range(10)), daemon=True),
    threading.Thread(target=monitor, args=(controls[1], string.ascii_lowercase), daemon=True)
]
for thread in threads:
    thread.start()

while True:
    event, values = window.read()
    if event == PySimpleGUI.WIN_CLOSED or event == 'Done':
        break

window.close()
