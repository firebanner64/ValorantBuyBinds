from pynput import keyboard
from pynput.keyboard import Listener, Controller, Key
from pynput.mouse import Button
from pynput.mouse import Controller as mController
import time

import config

_keyboard = Controller()
_mouse = mController()

def on_release(key):
    # checks if key has VK, and if the key is in the binds
    
    #print(key.name)
    #print(key.value)
    try:
        if not (coords := config.binds.get(key.vk, False)):
            print('not a bind')
            print(key.vk)
            return
    except AttributeError as e:
        print("no vk")
        return
    
    Buy(scale_res(coords))


def Buy(coords: tuple):
    buy_key = keyboard.KeyCode.from_vk(config.buy_menu)
    _keyboard.tap(buy_key)
    time.sleep(0.1)
    _mouse.position = coords
    _mouse.click(Button.left, 1)
    _keyboard.tap(buy_key)

def scale_res(coords: tuple):
    scale_factor = config.display_res[0] / coords[2]
    print(round(coords[0] * scale_factor), round(coords[1] * scale_factor))
    return (round(coords[0] * scale_factor), round(coords[1] * scale_factor))
    
# Add events

def start_listening():
    listener = Listener(on_release=on_release)
    
    listener.start()
    listener.join()
    


