# 创作者 马如云

from demo.screenshot import  screenshot
import numpy
from PIL import Image
import cv2
import pythoncom
from demo.formfocus import setf
import time
import threading
import math
from demo.operation import Operation
from numba import jit
import concurrent.futures






def Job_formfocus():#窗口焦点线程
    pythoncom.CoInitialize()
    sf = setf()
    while True:
        try:
            sf.setfocus()
        except Exception as e:
            print (e)




