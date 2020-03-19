# 创作者 马如云
import sys
sys.path.append('H:\\OpenAI')

from demo.screenshot import  screenshot
import numpy
import pyautogui
import cv2
from pynput.keyboard import Key, Controller
import gc
from demo.operation import Operation
import win32gui
from PyQt5.QtWidgets import QApplication
import time
from demo.get_key import key_check

# 判断是否退出
isQuit = 0



def chapter1():
   # 声明isQuit为全局变量
   global isQuit

   keyboard = Controller()
   op=Operation()
   app = QApplication(sys.argv)
   hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")  #建立qt的app实例，寻找对应游戏窗口的hwnd
   for i in range(10000):
      while isQuit == 0:
         start = cv2.getTickCount()# 计时函数

         image = screenshot(hWnd)

         img = numpy.asarray(image)#截图转换数组

         if (img[400,0]==numpy.array([254,31,111])).all():#如果颜色为粉色，则进入教学关第二部分，退出第一部分
            return

         finalmask = cv2.inRange(img, numpy.array([213, 240, 250]), numpy.array([225, 245, 252]))#二值化取出终点图像
         (finalcontours, _) = cv2.findContours(finalmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#图像梯度变换求轮廓
         gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0)
         gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1)
         gradient = cv2.subtract(gradX, gradY)

         gradient = cv2.convertScaleAbs(gradient)


         playermask = cv2.inRange(img, numpy.array([0, 230, 230]), numpy.array([120, 255, 255]))#图像二值化求玩家轮廓
         (playercontours, _) = cv2.findContours(playermask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         playercontours.sort(key=cv2.contourArea, reverse=True)#排序求出最大的那块即为玩家坐标


         if(len(finalcontours)<=0):
            break


         if len(playercontours) > 0:#能够寻找到玩家时
            cnt = playercontours[0]
            (playerX, playerY), playerR = cv2.minEnclosingCircle(cnt)#求外接圆圆形半径
            keyboard.press(Key.right)

            for i in range(0, int(2 * playerR), 1):
               for j in range(70,90):
                  if (gradient[min(899,int(i + playerY - playerR)), min(1599,int(playerX + playerR + j))] > 0):#如果附近有障碍物
                      op.escape()
            del cnt, playerX, playerY, playerR

         del playermask, playercontours,finalcontours,finalmask
         end = cv2.getTickCount()
         # print((end - start) / cv2.getTickFrequency())
         del start, end
         del image, gradient, gradY, gradX,gray,img

         # 点击T退出程序
         keys = key_check()
         if 'T' in keys:
             isQuit = 1
      # 退出for循环
      if isQuit == 1:
         keyboard.release(Key.right)#松开右箭头
         return

      keyboard.release(Key.right)


   del hWnd,keyboard,op
   gc.collect()#垃圾回收
   sys.exit(app.exec_())#安全退出


def chapter2():
   op = Operation()
   op.goRight(0.35)
   op.goUp(0.23)
   app = QApplication(sys.argv)
   time.sleep(35)#走到指定位置并且等待终点
   hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")  # ???????????????Visual Studio??SPY++??????
   while 1:
      print()
      image = screenshot(hWnd)

      img = numpy.asarray(image)

      playermask = cv2.inRange(img, numpy.array([0, 230, 230]), numpy.array([120, 255, 255]))#求出玩家轮廓
      (playercontours, _) = cv2.findContours(playermask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      playercontours.sort(key=cv2.contourArea, reverse=True)

      if len(playercontours) > 0:
         cnt = playercontours[0]
         (playerX, playerY), playerR = cv2.minEnclosingCircle(cnt)

         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#进行梯度轮廓变化
         gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0)
         gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1)
         gradient = cv2.subtract(gradX, gradY)

         gradient = cv2.convertScaleAbs(gradient)


         for i in range(0, int(2 * playerR), 1):
            for j in range(40, 60):
               if (gradient[min(899, int(i + playerY - playerR)), min(1599, int(playerX + playerR + j))] > 0):#判断右侧是否有障碍物
                  op.escape()
                  del app, hWnd
                  return

         del playerY, playerX, playerR

      del img, image, playercontours, playermask

def chapter3():
    op =Operation()
    op.goRight(1.2)
    del op


def main():
   chapter1()
   chapter2()

if __name__ == '__main__':
   main()