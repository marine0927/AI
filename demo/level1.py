# 创作者 马如云
import sys
sys.path.append('H:\\OpenAI')

from demo.screenshot import  screenshot
import numpy
import pyautogui
import cv2
from pynput.keyboard import Key, Controller
from numba import jit
import gc
from demo.operation import Operation
from cProfile import Profile
import win32gui
from PyQt5.QtWidgets import QApplication
import math
from demo.point import Point
import time

def main():
   keyboard = Controller()
   app = QApplication(sys.argv)
   hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")#载入qt的app实例，寻找游戏对应窗口的hwnd
   for i in range(10000):
      while 1:
         start = cv2.getTickCount()#程序计时

         image = screenshot(hWnd)

         img = numpy.asarray(image)
         print(img[0, 0])#输出背景色
         # if (img[0,0]==numpy.array([2,27,35])).all() or (img[0,0]==numpy.array([21,36,37])).all():
         #    print(1)
         #    return
         playermask = cv2.inRange(img, numpy.array([0, 230, 230]), numpy.array([120, 255, 255]))#二值化寻找玩家轮廓
         (playercontours, _) = cv2.findContours(playermask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         playercontours.sort(key=cv2.contourArea, reverse=True)
         if len(playercontours)<=0:
            return

         if len(playercontours) > 0:#求方块外接圆圆心和半径
            cnt = playercontours[0]
            (playerX, playerY), playerR = cv2.minEnclosingCircle(cnt)

            for i in range(0, 60):
                  if ((img[int(playerY+i), int(playerX + playerR+40)]==numpy.array([0,0,0])).all()==False):#判断障碍物，如果上方有障碍物，则往下移动
                     keyboard.press(Key.up)
                     time.sleep(0.01*i/20)
                     keyboard.release(Key.up)
                     break
                  if ((img[int(playerY-i), int(playerX + playerR+40)]==numpy.array([0,0,0])).all()==False):
                     keyboard.press(Key.down)
                     time.sleep(0.01*i/20)
                     keyboard.release(Key.down)
                     break

         end = cv2.getTickCount()
         print((end - start) / cv2.getTickFrequency())

   del hWnd,keyboard
   gc.collect()
   sys.exit(app.exec_())

def main2():
   keyboard = Controller()
   app = QApplication(sys.argv)
   hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")
   for i in range(10000):
      while 1:
         start = cv2.getTickCount()

         image = screenshot(hWnd)

         img = numpy.asarray(image)

         playermask = cv2.inRange(img, numpy.array([0, 230, 230]), numpy.array([120, 255, 255]))#二值化寻找玩家坐标
         (playercontours, _) = cv2.findContours(playermask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         playercontours.sort(key=cv2.contourArea, reverse=True)

         if len(playercontours) > 0:#求出玩家方块外接圆圆心和半径
            cnt = playercontours[0]
            (playerX, playerY), playerR = cv2.minEnclosingCircle(cnt)


            for i in range(0, 60):#检测障碍物方位，如果上方有障碍物，则向下躲避
               if ((img[int(playerY  +i), int(playerX + playerR+20)] == numpy.array([0, 0, 0])).all() == False):

                  keyboard.press(Key.up)
                  time.sleep(0.01*i/10)
                  keyboard.release(Key.up)
                  break
               if ((img[int(playerY - i), int(playerX + playerR+20)] == numpy.array([0, 0, 0])).all() == False):
                  keyboard.press(Key.down)
                  time.sleep(0.01*i/10)
                  keyboard.release(Key.down)
                  break



         end = cv2.getTickCount()
         print((end - start) / cv2.getTickFrequency())#输出时间间隔

   del hWnd, keyboard
   gc.collect()
   sys.exit(app.exec_())#垃圾回收，安全退出


if __name__ == '__main__':
   main()
   main2()