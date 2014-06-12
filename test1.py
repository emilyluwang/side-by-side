import httplib2
import urllib
from bs4 import BeautifulSoup, SoupStrainer
from BeautifulSoup import BeautifulStoneSoup

host_url = 'http://ec2-75-101-154-48.compute-1.amazonaws.com/node/12'

#http = httplib2.Http()
#status, response = http.request(host_url)

f = urllib.urlopen(host_url)
s = f.read()
f.close()

soup = BeautifulStoneSoup(s)


#for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
	#print link.attrs
    #if (link.get('href') != 'None'): 
    #if link.has_key('href'):
        #print link
	#print link.contents

stuff_to_parse = soup.findAll("a")
for each_link in stuff_to_parse:
    link = stuff_to_parse["href"]
    print link