# 创作者 马如云
# 主程序
from demo.screenshot import  screenshot
from demo.operation import Operation
from demo.formfocus import setf
from demo.move import Move
import win32api
import time
import pytesseract
import threading
import pythoncom
from demo import level0
from demo import  level1
from PyQt5.QtWidgets import QApplication
import sys
import win32gui
import os

op = Operation()


# 定义操作类
def Job_formfocus():#窗口焦点线程
    pythoncom.CoInitialize()# 线程初始化
    sf = setf()
    while True:
        time.sleep(3)
        try:
            sf.setfocus()
        except Exception as e:
            print(e)


def Job_gamestart():#打开游戏线程
    pythoncom.CoInitialize()
    app = QApplication(sys.argv)
    hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")  # 窗口的类名可以用Visual Studio的SPY++工具获取
    while True:
        img = screenshot(hWnd)  # 截图
        str1 = pytesseract.image_to_string(img)  # 文字识别
        # 判断动画是否已经加载完毕 q
        if str1.find('GAME') > 0:
            # 进入游戏
            op.enter()
            level0.main()#运行教学关算法
            break
    del app, hWnd

if __name__ == '__main__':
    # 打开游戏
    win32api.ShellExecute(0, 'open', r'F:\APP\JustShapes&Beats\JSB.exe', '', '', 1)
    # 运行线程
    thread_formfocus = threading.Thread(target=Job_formfocus, name="Job1", args=())
    thread_formfocus.start()
    thread_gamestart = threading.Thread(target=Job_gamestart, name="Job2", args=())
    thread_gamestart.start()
