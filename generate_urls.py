import os
import httplib2
import hashlib
import global_vars
from PIL import Image, ImageChops
from bs4 import BeautifulSoup, SoupStrainer

orig_url = 'http://www.balatarin.com/links/popular/recent/all/'

def get_balatarin_urls(url, lower_bound, upper_bound):

    url_list = []

    for i in range(lower_bound, upper_bound):

    	# getting the source code of the page at host_url
    	http = httplib2.Http()
    	status, response = http.request(url + str(i))
    	soup = BeautifulSoup(response, "lxml")

    	# filtering source code for only href tags
   		# extracts links from href tags
    	# then runs a commnand line process to screenshot all links
    	for tag in soup.findAll(attrs={"class": "content col-xs-11"}):
        	text_of_link = tag.h3.a['href'].encode('utf-8')
        	url_list.append(text_of_link)

    return url_list

for url in get_balatarin_urls(orig_url, 1, 5):
	print url