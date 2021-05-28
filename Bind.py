from pynput import keyboard
from pynput.keyboard import Listener, Controller, Key, KeyCode
from pynput.mouse import Button
from pynput.mouse import Controller as mController
import time
from PIL import ImageGrab

import config

_keyboard = Controller()
_mouse = mController()

def on_release(key):
    
    #find vk

    coords = config.binds.get(key.vk, False) if isinstance(key, KeyCode) else config.binds.get(key.value.vk, False) 

    print(coords)
    if not coords:
        print('not a bind')
        return
    
    Buy(scale_res(coords))


def Buy(scaled_coords: tuple):
    # open buy
    buy_key = keyboard.KeyCode.from_vk(config.buy_menu)
    _keyboard.tap(buy_key)
    time.sleep(0.1) #neeed

    #reset phantom
    _mouse.position = (0,0)
    _mouse.click(Button.left)
    time.sleep(0.3)#need

    # determine the action
    click_type = Button.right if is_purchased(scaled_coords) else Button.left
    
    #move to selected weapon and click
    _mouse.position = scaled_coords
    _mouse.click(click_type, 1)
    
    #close buy
    _keyboard.tap(buy_key)

def scale_res(coords: tuple):
    scale_factor = config.display_res[0] / coords[2]
    print(round(coords[0] * scale_factor), round(coords[1] * scale_factor))
    return (round(coords[0] * scale_factor), round(coords[1] * scale_factor))
    
# Add events

def get_pixel_color(scaled_coords: tuple):
    im = ImageGrab.grab()
    return im.getpixel(scaled_coords[0:2])

def is_purchased(scaled_coords: tuple):
    c = get_pixel_color(scaled_coords)
    print(c)

    return c[1] >= 75 # green value greater than 75

def start_listening():
    listener = Listener(on_release=on_release)
    
    listener.start()
    listener.join()
    


