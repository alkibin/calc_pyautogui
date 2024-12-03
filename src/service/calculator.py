import os
import pyautogui
import time
import psutil


class Calc:
    def __init__(self):
        self.pid = None

    def open(self):
        current_calc_pids = self.get_calc_processes_pid()
        os.system('calc')
        new_calc_pids = self.get_calc_processes_pid()
        self.pid = (new_calc_pids - current_calc_pids).pop()
        time.sleep(1)

    def get_calc_processes_pid(self):
        return {
            process.pid for process in
            psutil.process_iter(['pid', 'name', 'username'])
            if 'alculator' in process.info['name']
        }

    def close(self):
        psutil.Process(pid=self.pid).terminate()

    def _get_btn(self, btn_img):
        return pyautogui.locateOnScreen(btn_img, confidence=0.9)

    def _press_btn(self, pos, waiting=1):
        pyautogui.click(pos)

    def process_btn(self, btn_img, waiting=.5):
        pos = self._get_btn(btn_img)
        self._press_btn(pos)
        time.sleep(waiting)

    def get_result(self, t=2):
        time.sleep(t)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args, **kwargs):
        self.close()