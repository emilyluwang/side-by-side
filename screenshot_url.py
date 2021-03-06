import os
import httplib2
import hashlib
import global_vars
from PIL import Image, ImageChops
from bs4 import BeautifulSoup, SoupStrainer

def get_urls(url):

    url_list = []
    # getting the source code of the page at host_url
    http = httplib2.Http()
    status, response = http.request(url)
    soup = BeautifulSoup(response, "lxml")

    # filtering source code for only href tags
    # extracts links from href tags
    # then runs a commnand line process to screenshot all links
    for tag in soup.findAll('a', href = True):
        text_of_link = str(tag['href'])

        # if a link to an external website
        if 'http://' in text_of_link:
            url_list.append(text_of_link)

    return url_list

def clean_url(url):
    link_name = url[7:]
    
    # if there's an ending backslash    
    if '/' in link_name:
        
        # remove any backslashes or material after backslash
        # screenshot tool can't screenshot images with backslashes in their name
        sep = '/'
        rest = link_name.split(sep, 1)[0]
        return rest
    return link_name

def make_screenshots(list_of_urls):
    for url in list_of_urls:
        link_name = clean_url(url)

        # take screenshot of original page
        os.system('webkit2png -C -D ~/Desktop/images_temp -o ' + link_name + ' ' + url)

        # calculate hash
        new_hash = hashlib.md5(url)
        hash_link = global_vars.cache_url + new_hash.hexdigest() + '/'
        file_name = link_name + '_cache'

        os.system('webkit2png -C -D ~/Desktop/images_temp -o ' + file_name + ' ' + hash_link)


