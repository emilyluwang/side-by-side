import os
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

host_url = 'http://ec2-75-101-154-48.compute-1.amazonaws.com/node/12'
#os.system('webkit2png -F -D ~/Desktop/images_temp %s' % host_url)

http = httplib2.Http()
status, response = http.request(host_url)

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        text_of_link = link['href']
        if 'http://' in text_of_link:
            print text_of_link
            #os.system('webkit2png -F -D ~/Desktop/images_temp %s' % text_of_link)

