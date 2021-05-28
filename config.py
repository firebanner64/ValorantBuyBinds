# http://cherrytree.at/misc/vk.htm
import ctypes
user32 = ctypes.windll.user32
display_res = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(f"display is {display_res[0]} x {display_res[1]}")

# vk codes before, coords after
buy_menu = 66


#coord format (targetX, targetY, displayX, displayY) displayX/Y should be the resolution of the display that the coords were taken from
# COORDS MUST BE AN AREA IN THE BUY MENU THAT IS TRANSPARENT (NOT ON TEXT OR WEAPON MODEL)
_numpad = 96
binds = {
    (_numpad + 0):(1982,612,2560,1440), # heavy armor
    (_numpad + 1):(1185,744,2560,1440), #phantom
    (_numpad + 2):(1178,944,2560,1440), #vandal
    (_numpad + 3):(1543,533,2560,1440), # awp (you will buy this and die in 30 seconds don't)
    (_numpad + 4):(983,529,2560,1440), # spectre
    (_numpad + 5):(996,940,2560,1440), #judge
    (_numpad + 6):(1656,322,2560,1440), #marshall
    (_numpad + 7):(682,786,2560,1440), # ghost
    (_numpad + 8):(677,931,2560,1440), # sherrif, wow the ego
    (_numpad + 9):(675,607,2560,1440), # frenzy 
    
}

