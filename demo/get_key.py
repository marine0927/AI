# Developed by Chris Liu
# update by 高战立
import win32api as wapi

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
            # 0x20为space按键的16进制表示
        elif wapi.GetAsyncKeyState(0x20):
            keys.append('space')
    return keys