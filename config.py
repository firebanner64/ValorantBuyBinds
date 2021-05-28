# http://cherrytree.at/misc/vk.htm
import ctypes
user32 = ctypes.windll.user32
display_res = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(f"display is {display_res[0]} x {display_res[1]}")

# vk codes before, coords after (2560 x 1440)
buy_menu = 66


#coord format (targetX, targetY, displayX, displayY) displayX/Y should be the resolution of the display that the coords were taken from

_numpad = 96
binds = {
    (_numpad + 0):(1436, 668, 1920, 1080), # heavy armor


}

