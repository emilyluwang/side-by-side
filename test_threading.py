import os
import httplib2
import hashlib
import global_vars
import threading
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
        text_of_link = str(tag.contents[0])
        
        # if a link to an external website
        if 'http://' in text_of_link:
            url_list.append(text_of_link)

    return url_list

def clean_url(url):
    link_name = url[7:]
        #if there's an ending backslash
        
    if '/' in link_name:
        #remove the last backslash
        sep = '/'
        rest = link_name.split(sep, 1)[0]
        return rest
    return link_name

def make_screenshots(url):
 
    link_name = clean_url(url)

    # take screenshot of original page
    os.system('webkit2png -C -D ~/Desktop/images_temp -o' + link_name + ' ' + url)

    # calculate hash
    new_hash = hashlib.md5(url)
    hash_link = global_vars.cache_url + new_hash.hexdigest() + '/'
    file_name = link_name + '_cache'

    os.system('webkit2png -C -D ~/Desktop/images_temp -o ' + file_name + ' ' + hash_link)


def process(items, start, end):                                                 
    for item in items[start:end]:                                               
        try:                                                                    
            make_screenshots(item)                                              
        except Exception:                                                       
            print('error with item')      

def split_processing(items, num_splits=25):                                      
    split_size = len(items) // num_splits                                       
    threads = []                                                                
    for i in range(num_splits):                                                 
        # determine the indices of the list this thread will handle             
        start = i * split_size                                                  
        # special case on the last chunk to account for uneven splits           
        end = None if i+1 == num_splits else (i+1) * split_size                 
        # create the thread                                                     
        threads.append(                                                         
            threading.Thread(target=process, args=(items, start, end)))         
        threads[-1].start() # start the thread we just created                  

    # wait for all threads to finish                                            
    for t in threads:                                                           
        t.join()                                                                


split_processing(get_urls(global_vars.host_url))
