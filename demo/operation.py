# 创作者 马如云
# 键盘操作类
import pyautogui
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
class Operation:
    def __init__(self):
        return
    def goRight(self,interval):#移动指令 输入时间间隔
        keyboard.press(Key.right)
        time.sleep(interval)
        keyboard.release(Key.right)
    def goLeft(self,interval):
        keyboard.press(Key.left)
        time.sleep(interval)
        keyboard.release(Key.left)
    def goUp(self,interval):
        keyboard.press(Key.up)
        time.sleep(interval)
        keyboard.release(Key.up)
    def goDown(self,interval):
        keyboard.press(Key.down)
        time.sleep(interval)
        keyboard.release(Key.down)
    def goDownWithSpace(self,interval):#使用空格
        keyboard.press(Key.down)
        keyboard.press(Key.space)
        time.sleep(interval)
        keyboard.release(Key.space)
        keyboard.release(Key.down)
    def goUpWithSpace(self,interval):#使用空格
        keyboard.press(Key.up)
        keyboard.press(Key.space)
        time.sleep(interval)
        keyboard.release(Key.space)
        keyboard.release(Key.up)
    def goLeftWithSpace(self,interval):#使用空格
        keyboard.press(Key.left)
        keyboard.press(Key.space)
        time.sleep(interval)
        keyboard.release(Key.space)
        keyboard.release(Key.left)
    def goRightWithSpace(self,interval):#使用空格
        keyboard.press(Key.right)
        keyboard.press(Key.space)
        time.sleep(interval)
        keyboard.release(Key.space)
        keyboard.release(Key.right)
    def enter(self):# 按回车
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    def escape(self):# 按空格
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    def doNothing(self,interval):#不动
        return