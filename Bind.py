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

    print('acceptable')
    Buy(coords)


def Buy(coords: tuple):
    print('buying')
    buy_key = keyboard.KeyCode.from_vk(config.buy_menu)
    _keyboard.tap(buy_key)
    time.sleep(0.1)
    _mouse.position = coords
    _mouse.click(Button.left, 1)
    _keyboard.tap(buy_key)
    
    
# Add events

def start_listening():
    listener = Listener(on_release=on_release)
    
    listener.start()
    listener.join()
    


