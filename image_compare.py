import scipy 
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d
import Image
import global_vars

# now we obtain a difference image of the two screenshots
#im1 = Image.open(str(img_filepath + link_name + '-clipped.png'))
#im2 = Image.open(str(img_filepath + file_name + '-clipped.png'))
#diff = ImageChops.difference(im2, im1)
#diff.show()

# calculate the minimum bounding box to quantify the difference image
#print diff.getbbox()

def get(file_name):
	
	# get JPG image as Scipy array, RGB (3 layer)
	data = Image.open(file_name + '.png')
	data.save(file_name + '.jpg')

	data = imread(file_name + '.jpg')

	# convert to grey-scale using W3C luminance calc
	data = scipy.inner(data, [299, 587, 114]) / 1000.0

	# normalize per http://en.wikipedia.org/wiki/Cross-correlation
	return (data - data.mean()) / data.std()

def compare_images(file_name_1, file_name_2):
	img1 = get(global_vars.img_filepath + file_name_1 + '-clipped')
	img2 = get(global_vars.img_filepath + file_name_2 + '-clipped')

	c11 = c2d(img1, img1, mode='same') 
	c12 = c2d(img1, img2, mode='same')
	
	print c11.max(), c12.max()
