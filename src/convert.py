
f = open("./getvalue")
k =  f.read().split("\r\n")
for item in k:
    data = item.split(" ")
    tenbase = []
    for num in data:
        try:
            tenbase.append(int(num,16))
        except Exception:
            pass
    print "adb shell sendevent /dev/input/event3 {} {} {}".format(str(tenbase[0]),str(tenbase[1]),str(tenbase[2]))




