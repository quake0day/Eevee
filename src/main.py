# -*- coding: utf-8 -*-
import os
import subprocess
import telnetlib
from time import sleep

PHONE_IP = "192.168.1.110"
WECHAT = "-a android.intent.action.MAIN -n com.tencent.mm/.ui.LauncherUI"

class ADB:

    def __init__(self):
        self.address = PHONE_IP
        self.port = "5555"

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

    def refresh_Wechat(self):
        adb_press_event_enter = "adb shell input keyevent 66" # press Enter
        adb_press_event_esc  = "adb shell input keyevent 4" # press Esc
        adb_press_event_down  = "adb shell input keyevent 20" # press down arrow
        try:
            handler = subprocess.Popen(adb_press_event_enter,shell=True)
            handler.wait()
            sleep(8)
            i = 0
            while i < 100:
                handler = subprocess.Popen(adb_press_event_down,shell=True)
#                handler.wait()
                sleep(0.1)
                i = i + 1
            handler = subprocess.Popen(adb_press_event_esc,shell=True)
            handler.wait()

        except Exception,E:
            print "Cannot send keycode "
            return 1


        




class Telnet:

    def __init__(self):
        self.address = PHONE_IP
        self.port = "5330"

    def enable_gpsSpoof(self):
        try:
            self.t = telnetlib.Telnet()
            self.t.open(self.address,self.port)
            sleep(1)
            self.t.read_until("$")
            sleep(1)
            self.t.write("geo gpsSpoofer start" +'\r\n')
            return 0
        except Exception,E:
            print "Cannot telnet to androVM, check ip and port and maybe you need install and enable Android developer shell first"
            return 1

    def gpsSpoof(self,lat,lng):
        gpsSpoof_command = "geo gpsSpoofer fix {} {} \r\n".format(str(lat),str(lng))
        try:
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




adb = ADB()
tel = Telnet()
tel.enable_gpsSpoof()
adb.connect()
#adb.start(WECHAT)
adb.refresh_Wechat()

#tel = Telnet()
#tel.telnet()
#tel.enable_gpsSpoof()
tel.gpsSpoof("37","114")
adb.refresh_Wechat()
tel.gpsSpoof("38","115")
adb.refresh_Wechat()
