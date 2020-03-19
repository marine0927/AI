# 创作者 马如云
# 截屏函数
from PIL import Image
from PyQt5.QtWidgets import QApplication
import win32gui
import numpy
import sys
import gc


def screenshot(hWnd):
    # 获取后台窗口的句柄，注意后台窗口不能最小化'
    screen = QApplication.primaryScreen()
    image = screen.grabWindow(hWnd).toImage()
    img=Image.fromqpixmap(image)#转化图片的类别
    del hWnd,screen,image
    return img


