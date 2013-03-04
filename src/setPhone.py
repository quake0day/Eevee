# -*- coding: utf-8 -*-
import os
import subprocess
import telnetlib
import zmq
from time import sleep
import getHeight as gh

PHONE_IP = "192.168.0.59"
WECHAT = "-a android.intent.action.MAIN -n com.tencent.mm/.ui.LauncherUI"

class ADB:

    def __init__(self):
        self.address = PHONE_IP
        self.port = "5555"
        self.first = True

    def connect(self):
        adb_conn_command = "adb connect {}:{}".format(str(self.address),str(self.port)) 
        try:
            handler = subprocess.Popen(adb_conn_command,shell=True)
            handler.wait()
        except Exception,E:
            print "Cannot connect to androVM through adb, check the ip and port"
            return 1

    # Start Wechat but need user to click
    def start(self,appname):
        adb_start_command = "adb shell am start {}".format(str(appname))
        try:
            handler = subprocess.Popen(adb_start_command,shell=True)
            handler.wait()
        except Exception,E:
            print "Cannot start Wechat"
            return 1

    # not finished
    def init_weixin(self):
        return 0

    def set_Wechat(self):
        adb_press_event_enter = "adb shell input keyevent 66" # press Enter
        adb_press_event_esc  = "adb shell input keyevent 4" # press Esc
        adb_press_event_down  = "adb shell input keyevent 20" # press down arrow
        handler = subprocess.Popen(adb_press_event_down,shell=True)
        handler.wait()
        handler = subprocess.Popen(adb_press_event_down,shell=True)
        handler.wait()
        handler = subprocess.Popen(adb_press_event_down,shell=True)
        handler.wait()
        handler = subprocess.Popen(adb_press_event_down,shell=True)
        handler.wait()
        handler = subprocess.Popen(adb_press_event_down,shell=True)
        handler.wait()


    def refresh_Wechat(self):
        adb_press_event_enter = "adb shell input keyevent 66" # press Enter
        adb_press_event_esc  = "adb shell input keyevent 4" # press Esc
        adb_press_event_down  = "adb shell input keyevent 20" # press down arrow
        try:
            if(self.first != True):
                sleep(0.1)
            else:
                self.first = False
            handler = subprocess.Popen(adb_press_event_enter,shell=True)
            handler.wait()
            sleep(10)
            i = 0
            while i < 50:
                handler = subprocess.Popen(adb_press_event_down,shell=True)
                #handler.wait()
                sleep(0.4)
                i = i + 1
            handler = subprocess.Popen(adb_press_event_esc,shell=True)
            handler.wait()
        except Exception,E:
            print E
            print "Cannot send keycode "
            return 1

class Telnet:

    def __init__(self):
        self.address = PHONE_IP
        self.port = "5330"

    def establish_conn(self):
        try:
            self.t = telnetlib.Telnet()
            self.t.open(self.address,self.port)
            sleep(1)
            self.t.read_until("$")
        except Exception,E:
            print "Cannot telnet to androVM, check ip and port and maybe you need install and enable Android developer shell first"
            return 1

    def enable_gpsSpoof(self):
        try:
            sleep(1)
            self.t.write("geo gpsSpoofer start" +'\r\n')
        except Exception,E:
            print "Cannot enable gps spoofer"
            return 1

    def disable_gpsSpoof(self):
        try:
            self.t.write("geo gpsSpoofer stop" +'\r\n')
        except Exception,E:
            print "Cannot disable gps spoofer"
            return 1

    def gpsSpoof(self,lat,lng):
        gpsSpoof_command = "geo gpsSpoofer fix {} {} \r\n".format(str(lat),str(lng))
        try:
            self.t.read_until("$")
            self.t.write(gpsSpoof_command)
            sleep(1)
        except Exception,E:
            print E
            print "cannot change gps check if gpsSpoof is enabled"
            return 1

    # broken
    def quit(self):
        self.t.write("exit \r\n")
        sleep(1)
        self.t.write("exit \r\n")
        self.t.close()
        return 0


def load_loc():
    #geo = gh.formatPathInfo(gh.getPathInfo(42.99855039261829,-78.79622441563413,43.004905938753645,-78.78722492218014))  #TEST 2
    #geo = gh.formatPathInfo(gh.getPathInfo(43.000002025901935, -78.79973274502561,43.000002025901935, -78.78740731239316))  #TEST 3
    geo = gh.formatPathInfo(gh.getPathInfo(43.000002025901935, -78.79973274502561,43.000002025901935,-78.68290844917294))  #TEST 3
    return geo

adb = ADB()
#tel = Telnet()
#tel.establish_conn()
#tel.enable_gpsSpoof()
adb.connect()
#adb.start(WECHAT)
#adb.refresh_Wechat()
adb.set_Wechat()

#tel = Telnet()
#tel.telnet()
#tel.enable_gpsSpoof()
"""
geo = load_loc()
i = 0
for item in geo:
    show = "TEST:"+str(i)
    print show
    i = i + 1
    print item[0],item[1]
    tel.disable_gpsSpoof()
    tel.enable_gpsSpoof()
    tel.gpsSpoof(item[0],item[1])
    #tel.gpsSpoof(39.9435576704414,116.43685933589938)
    adb.refresh_Wechat()
geo = load_loc()
i = 0
for item in geo:
    print i
    print item[0],item[1]
    i = i + 1
    """
