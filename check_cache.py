import global_vars
import image_compare
import screenshot_url

def generate_comparisons():
	# empty text files
	f = open(global_vars.failed_pages, 'w')
	f.close()

	f = open(global_vars.comparison_results, 'w')
	f.close()

	# get list of urls to cache on host page
	links_to_cache = screenshot_url.get_urls(global_vars.host_url)

	# screenshot these urls
	#screenshot_url.make_screenshots(links_to_cache)

	# run image comparison on original url screenshot and cached url screenshot
	for link in links_to_cache:
		new_link = screenshot_url.clean_url(link)
		image_compare.compare_images(link, new_link, new_link + '_cache')

generate_comparisons()