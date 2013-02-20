import re
from getelevation import getGoogleElevationData

#def getPathInfo(running_id):
#    conn = connMysql()
#    cur = conn.cursor()
#    sql = "select path_info FROM `main` where `running_id` ="+str(running_id)+\
#            " order by id desc"
#    cur.execute(sql)
#    path_info = cur.fetchone()
#    cur.close()
#    conn.close()
#    return path_info
#
def getPathInfo(lat1,lng1,lat2,lng2):
###### Change HERE!!!!!!!!!!!!!!
    startStr = str(lat1)+","+str(lng1)
    endStr = str(lat2)+","+str(lng2)
    pathStr = startStr + "|" + endStr
    data = getGoogleElevationData(pathStr)
    return data





def formatPathInfo(path_info):
#    print path_info
    geo_dataset = []
    for resultset in path_info['results']:
        dataset = []
        dataset.append(resultset["location"]['lat'])
        dataset.append(resultset["location"]['lng'])
        geo_dataset.append(dataset)
    return geo_dataset
            
#@formatPathInfo(getpathinfo(90,-118,50,-116))

def getHTT(geo_height):
    return float(geo_height[0][2])

def getHRR(geo_height):
    return float(geo_height[-1][2])

#geo = formatPathInfo(getPathInfo("15"))
#print geo
#print getHRR(geo)

#geo = formatPathInfo(getPathInfo(33,44,33,55))
#print geo
