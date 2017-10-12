import urllib2
response = urllib2.urlopen("http://www.jd.com")
print response.read()