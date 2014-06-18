import scipy 
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d
import Image
import global_vars
import os.path
import hashlib

def get(file_name):
	
	# get JPG image as Scipy array, RGB (3 layer)
	data = Image.open(file_name + '.png')
	data.save(file_name + '.jpg')

	data = imread(file_name + '.jpg')

	# convert to grey-scale using W3C luminance calc
	data = scipy.inner(data, [299, 587, 114]) / 1000.0

	# normalize per http://en.wikipedia.org/wiki/Cross-correlation
	return (data - data.mean()) / data.std()

def compare_images(orig_url, file_name_1, file_name_2):
	file_path_1 = global_vars.img_filepath + file_name_1 + '-clipped'
	file_path_2 = global_vars.img_filepath + file_name_2 + '-clipped' 
	
	hash_of_url = hashlib.md5(orig_url)
	hash_link = global_vars.cache_url + hash_of_url.hexdigest() + '/'

	f1_open = False

	if os.path.isfile(file_path_1 + '.png'):
		img1 = get(file_path_1)
		f1_open = True
	else:
  		f = open(global_vars.failed_pages, 'a')
  		f.write(file_name_1 + "\n")
  		f.close()

  	if os.path.isfile(file_path_2 + '.png'):
  		if f1_open == True:
  			img2 = get(file_path_2)
  			#c11 = c2d(img1, img1, mode='same') 
			c12 = c2d(img1, img2, mode='same')
			diff = c12.max()
			skew = c12.max()/30000.

			# write results to results file
			f = open(global_vars.comparison_results, 'a')
			f.write(file_name_1 + ',' + file_name_2 + ',' + orig_url + ',' + hash_link + ',' + str(skew) + "\n")
			f.close()

	else:
		f = open(global_vars.failed_pages, 'a')
		f.write(file_name_2 + "\n")
		f.close()
