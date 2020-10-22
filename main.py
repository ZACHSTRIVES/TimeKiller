from pynput import mouse, keyboard
import threading
import time

actions = True


class TimeKiller:
    def __init__(self):
        self.__is_actions = True

    def timer_thread(self):
        while True:
            time.sleep(10)
            if self.__is_actions:
                self.__is_actions = False
            else:
                print("执行：timer——thread")

    def on_click(self, x, y, button, pressed):  # 鼠标点击监听器
        self.__is_actions = True

    def on_move(self, x, y):  # 鼠标移动监听器
        self.__is_actions = True

    def on_press(self, key):  # 键盘输入监听器
        self.__is_actions = True

    def action_listener_thread(self):
        while True:
            with mouse.Listener(on_click=self.on_click, on_move=self.on_move) as listener:
                listener.join()
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()

    def start(self):
        threads = [threading.Thread(target=TimeKiller.action_listener_thread, args=(self,)),
                   threading.Thread(target=TimeKiller.timer_thread, args=(self,))]
        for i in threads:
            i.start()


tk = TimeKiller()
tk.start()
