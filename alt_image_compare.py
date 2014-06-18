import Image
import ImageChops

img_filepath = '../../../Desktop/images_temp/r10.net-clipped.jpg'
img_2_filepath = '../../../Desktop/images_temp/r10.net_cache-clipped.jpg'

# now we obtain a difference image of the two screenshots
im1 = Image.open(str(img_filepath))
im2 = Image.open(str(img_2_filepath))
diff = ImageChops.difference(im2, im1)

print diff.size