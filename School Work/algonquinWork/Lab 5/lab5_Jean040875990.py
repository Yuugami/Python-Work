import pycurl
import xml.etree.ElementTree as bus
import webbrowser
from StringIO import StringIO

def getOCData(stopNo, routeNo):
	postfield = "appID=3875e418&apiKey=ea5f5d83fd97bc2d2b311c745cf3585b&stopNo=" \
	+ str(stopNo) + "&routeNo=" + str(routeNo) + "&format=xml";
	c = pycurl.Curl()
	c.setopt(pycurl.POST, True )
	c.setopt(pycurl.POSTFIELDS, postfield)
	c.setopt(pycurl.URL, 'https://api.octranspo1.com/v1.2/GetNextTripsForStop')
	c.setopt(pycurl.SSL_VERIFYHOST,0)
	c.setopt(pycurl.SSL_VERIFYPEER,0)
	buffer = StringIO()
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	return buffer


def doIt(stopNo, routeNo):
     lst = []
     doc = bus.fromstring(getOCData(stopNo, routeNo).getvalue().decode('utf-8'))     # Your shortened XML document
   
     for b in doc.findall('.//{http://tempuri.org/}Trip'):
          lat = b.findtext('{http://tempuri.org/}Latitude')
          lon = b.findtext('{http://tempuri.org/}Longitude')
          start = b.findtext('{http://tempuri.org/}TripStartTime')
          print tuple((lat,lon,start))
          lst .append(tuple((lat,lon,start)))
     for l in lst:
          webbrowser.open_new("https://www.google.ca/maps/place//@" \
               + str(l[0]) + "," + str(l[1]) + ",20z" + \
               "/data=!3m1!4b1!4m2!3m1!1s0x0:0x0")

if __name__ == '__main__':
	stopNo = int(input("Enter a bus stop number: "))
	routeNo = int(input("Enter a bus route number: "))
	doIt(stopNo, routeNo);
