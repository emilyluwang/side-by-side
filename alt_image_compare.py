import Image
import ImageChops
import os

img_name = "../../../Desktop/images_temp/softpedia.com-clipped"
img_filepath = '../../../Desktop/images_temp/softpedia.com-clipped.jpg'
img_2_filepath = '../../../Desktop/images_temp/softpedia.com_cache-clipped.jpg'

# now we obtain a difference image of the two screenshots
im1 = Image.open(str(img_filepath))
im2 = Image.open(str(img_2_filepath))
diff = ImageChops.difference(im2, im1)
diff.save(img_name + "_diff", "JPEG")

print os.path.getsize(img_name + "_diff")