import urllib2,urllib
params = {}
params['app'] = "wechat-buffalo"
params['user'] = 'quakezzz'
params = urllib.urlencode(params)
u = urllib2.urlopen('http://202.120.38.222:8080/submit-trace',params)
print u.read()
