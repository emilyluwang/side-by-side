import global_vars
import image_compare
import screenshot_url

def generate_comparisons():

	print("getting links to cache...")
	# get list of urls to cache on host page
	links_to_cache = screenshot_url.get_urls(global_vars.host_url)

	# screenshot these urls
	print("making screenshots...")
	screenshot_url.make_screenshots(links_to_cache)

	# run image comparison on original url screenshot and cached url screenshot
	print("comparing screenshots...")
	for link in links_to_cache:
		link = screenshot_url.clean_url(link)
		image_compare.compare_images(link, link + '_cache')

generate_comparisons()