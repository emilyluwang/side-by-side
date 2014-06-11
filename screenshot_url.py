import os
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

# the page containing all links to visit and screenshot
host_url = 'http://ec2-75-101-154-48.compute-1.amazonaws.com/node/12'
cach_url = 'http://ec2-75-101-154-48.compute-1.amazonaws.com/CAYL/cache/'

# getting the source code of the page at host_url
http = httplib2.Http()
status, response = http.request(host_url)

# filtering source code for only href tags
# extracts links from href tags
# then runs a commnand line process to screenshot all links
for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        text_of_link = link['href']
        if 'http://' in text_of_link:
            # figure out some way to calculate hash of link as well
            print text_of_link
            os.system('webkit2png -F -D ~/Desktop/images_temp %s' % text_of_link)
            # now we need to calculate hash

