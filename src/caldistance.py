'''
#=============================================================================
#     FileName: caldistance.py
#         Desc: cal the distance between two latlng pairs
#               The return value is KM
#       Author: quake0day
#        Email: quake0day@gmail.com
#     HomePage: http://www.darlingtree.com
#      Version: 0.0.1
#   LastChange: 2012-04-04 15:37:22
#      History:
#=============================================================================
'''
import math
import sys 


EARTH_RADIUS = 6378137.0

def rad(d):
    return float(d)*math.pi/180.0

def CalDis(lat1,lng1,lat2,lng2):
    radlat1 = rad(lat1)
    radlat2 = rad(lat2)
    radlng1 = rad(lng1)
    radlng2 = rad(lng2)
    con = math.sin(radlat1)*math.sin(radlat2)
    con += math.cos(radlat1)*math.cos(radlat2)*math.cos(radlng1-radlng2)
    return math.acos(con)*EARTH_RADIUS/1000
   # b = rad(lng1) - rad(lng2)
   # s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2),2) + \
   #     math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
    #print s
   # s = round(s*10000)/10000 
   # return s


    


if __name__== '__main__':
    try:
        lat1 = float(sys.argv[1])
        lng1 = float(sys.argv[2])
        lat2 = float(sys.argv[3])
        lng2 = float(sys.argv[4])
    except IndexError,e:
        sys.exit()
    distance = CalDis(lat1,lng1,lat2,lng2)
    print distance
 #   if distance == 0: # success


