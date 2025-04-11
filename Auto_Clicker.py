import pyautogui
import time

def auto_clicker(x, y, interval, clicks):
    for _ in range(clicks):
        pyautogui.click(x, y)
        time.sleep(interval)

auto_clicker(500, 500, 0.5, 10)
