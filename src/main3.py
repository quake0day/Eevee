# -*- coding: utf-8 -*-
import os
import subprocess
import telnetlib
import socket
from time import sleep

PHONE_IP = "192.168.1.108"
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

    def refresh_Wechat(self):
        adb_press_event_enter = "adb shell input keyevent 66" # press Enter
        adb_press_event_esc  = "adb shell input keyevent 4" # press Esc
        adb_press_event_down  = "adb shell input keyevent 20" # press down arrow
        try:
            if(self.first != True):
                self.f = open("./tmp","w")
                self.f.write("0")
                self.f.close()
            else:
                self.first = False
            handler = subprocess.Popen(adb_press_event_enter,shell=True)
            handler.wait()
            msg = "0"
            while msg != "1":
                sleep(0.1)
                self.f = open("./tmp","w")
                msg = self.f.read()
                print msg
            i = 0
            while i < 100:
                handler = subprocess.Popen(adb_press_event_down,shell=True)
                sleep(0.3)
                i = i + 1
            handler.wait()
            handler = subprocess.Popen(adb_press_event_esc,shell=True)
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



"""
if __name__ == '__main__':    
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    if os.path.exists('/tmp/UNIX.d'):
        os.unlink('/tmp/UNIX.d')
    sock.bind('/tmp/UNIX.d')   
    sock.listen(5)   
    while True:
        connection,address = sock.accept()    
        #print "%s"%connection.recv(1024);
        user_info = connection.recv(1024);
        print user_info.split("Within")[0]
        print user_info.split("Within")[1]
        connection.close() 
"""



#adb = ADB()
tel = Telnet()
tel.establish_conn()
tel.enable_gpsSpoof()
i = 90
tel.gpsSpoof(39.9339-0.005*i,116.362-0.005*i)
#adb.connect()
#adb.start(WECHAT)
#adb.refresh_Wechat()

"""
#tel = Telnet()
#tel.telnet()
#tel.enable_gpsSpoof()
i = 0

while i < 10:
    print (39.9339-0.05*i)
    print (116.362-0.05*i)
    tel.disable_gpsSpoof()
    tel.enable_gpsSpoof()
    tel.gpsSpoof(39.9339-0.005*i,116.362-0.005*i)
    adb.refresh_Wechat()
    i = i + 1

    """
