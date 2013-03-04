import sys
import os
import time

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
device = MonkeyRunner.waitForConnection(99, "015d3b661f20020a")



def click(left, top):
    global device
    device.touch(left, top, MonkeyDevice.DOWN_AND_UP)

def drag(start, end):
    global device
    device.drag(start, end, 3, 5)

def refresh():
    time.sleep(1)
    click(250, 1253)
    time.sleep(2)
    click(115, 1180)
    time.sleep(2)
    drag((470, 200), (470, 900))
    time.sleep(10)
    click(571, 1171)
    time.sleep(2)
    click(490, 206)
    time.sleep(2)
    drag((470, 200), (470, 900))
    time.sleep(8)

refresh()
