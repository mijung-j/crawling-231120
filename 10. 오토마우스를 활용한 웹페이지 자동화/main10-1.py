import pyautogui
# pip install PyAutoGUI
# conda install -c conda-forge pyautogui
import time

class Weather:
    def __init__(self):
        self.region = ''

    def set_region(self, region):
        self.region = region

    def _(self):
        while True:
            print(pyautogui.position())
            time.sleep(0.1)

if __name__ == '__main__':
    w = Weather()
    w._()