import sys
import os
import time

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
#device = MonkeyRunner.waitForConnection(99, "015d3b661f20020a")
device = MonkeyRunner.waitForConnection()



def click(left, top):
    global device
    device.touch(left, top, MonkeyDevice.DOWN_AND_UP)

def drag(start, end):
    global device
    device.drag(start, end, 3, 5)

def refresh():
    global device
    time.sleep(1)
   # click(62, 78)
    click(108,225)
    time.sleep(15)
   # click(659, 313)
    for i in range(1,10):
        device.drag((250,850),(250,110),0.1,10)
    MonkeyRunner.sleep(1)
    click(39,51)

refresh()
