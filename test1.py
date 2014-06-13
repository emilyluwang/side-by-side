import httplib2
import lxml
import urllib
from bs4 import BeautifulSoup, SoupStrainer

host_url = 'http://ec2-75-101-154-48.compute-1.amazonaws.com/node/12'

http = httplib2.Http()
status, response = http.request(host_url)

soup = BeautifulSoup(response, "lxml")

#f = urllib.urlopen(host_url)
#s = f.read()
#f.close()

#soup = BeautifulSoup(s)


#for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
	#print link.attrs
    #if (link.get('href') != 'None'): 
    #if link.has_key('href'):
        #print link
	#print link.contents

for tag in soup.findAll('a', href = True):
	link_name = str(tag.contents[0])

	if 'http://' in link_name:
		print link_name
#for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
	#print link
	




#stuff_to_parse = soup.findAll("a")
#for each_link in stuff_to_parse:
    #link = stuff_to_parse['href']
    #print link