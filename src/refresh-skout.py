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
    click(411, 1250)
    print "Here"
    time.sleep(2)
    click(721, 1155)
    time.sleep(2)
    click(474, 529)
    time.sleep(4)
    drag((470, 200), (470, 900))
    time.sleep(12)

refresh()
