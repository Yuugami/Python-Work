import pycurl
import xml.etree.ElementTree as bus
import webbrowser
from StringIO import StringIO

def getOCData():
	c = pycurl.Curl()
	c.setopt(pycurl.POST, True )
	c.setopt(pycurl.POSTFIELDS,'appID=3875e418&apiKey=ea5f5d83fd97bc2d2b311c745cf3585b&stopNo=3004&routeNo=97&format=xml')
	c.setopt(pycurl.URL, 'https://api.octranspo1.com/v1.2/GetNextTripsForStop')
	c.setopt(pycurl.SSL_VERIFYHOST,0)
	c.setopt(pycurl.SSL_VERIFYPEER,0)
	buffer = StringIO()
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	return buffer


def doIt():
   lst = []
   doc = bus.fromstring(getOCData().getvalue().decode('utf-8'))     # Your shortened XML document
   
   for b in doc.findall('.//{http://tempuri.org/}Trip'):
		lat = b.findtext('{http://tempuri.org/}Latitude')
		lon = b.findtext('{http://tempuri.org/}Longitude')
		start = b.findtext('{http://tempuri.org/}TripStartTime')
		print tuple((lat,lon,start))
		lst .append(tuple((lat,lon,start)))
   for l in lst:
		print l[0],l[1],l[2]
	

if __name__ == '__main__':
    doIt()
