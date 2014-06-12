import httplib2
from bs4 import BeautifulSoup, SoupStrainer

host_url = 'http://ec2-75-101-154-48.compute-1.amazonaws.com/node/12'

http = httplib2.Http()
status, response = http.request(host_url)

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
	print link.attrs
    #if (link.get('href') != 'None'): 
    #if link.has_key('href'):
        #print link
