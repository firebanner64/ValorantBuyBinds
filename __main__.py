
import pynput
import time
from pynput.mouse import Button, Controller
import Bind

mouse = Controller()

Bind.start_listening()

while True:
    print(mouse.position)
    time.sleep(0.5)
    



