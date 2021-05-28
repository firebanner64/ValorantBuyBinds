
import pynput
import time
from pynput.mouse import Button, Controller
import Bind
from PIL import ImageGrab
from colour import Color

mouse = Controller()
print('im hatsune miku')
Bind.start_listening()

while True:
    print(mouse.position)
    #im = ImageGrab.grab()
    #rgb=im.getpixel(mouse.position)

    #rgb = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255,
    #c = Color(rgb=rgb)
    #print(c.hsl)
    time.sleep(0.5)


