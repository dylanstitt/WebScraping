# Dylan Stitt
# A collection of functions to use for basic webscraping

import requests

# Clean the results for a clean output into the console or another file
def cleanResults(results):
	results = results.text.splitlines()
	temp = []
	for text in results:
		if text not in ['', '\n']:
			temp.append(text.strip())

	return '\n'.join(temp)

# Create a file to write the contents to it or just create a file
def createFile(filename, mode, content=None):
	with open(filename, mode) as file:
		if content != None: 
			if isinstance(content, dict):
				for key in content:
					file.write(f'{key}: \n\n {content[key]}\n')
			else: file.write(content)
		else: file.write('')

# Read the contents of a file
def readFile(filename, contentType):
	with open(filename, 'r') as file:
		if contentType == 'list':
			return file.read().splitlines()
		else:
			return file.read()

################################################################################################
#                                     Scraping Functions                                       #
################################################################################################

# Scrape any tag
def scrapeTag(soupObject, tag):
	return soupObject.find_all(tag)

# Scrape an element by the id
def scrapeId(soupObject, ID):
	return soupObject.find_all(id=ID)

# Scrape the element by the class 
def scrapeClass(soupObject, CLASS):
	return soupObject.find_all(class_=CLASS)

# Scrape the title of the article/page
def scrapeTitle(soupObject, mainElement, titleElement):
	results = soupObject.find(mainElement)
	tag = results.find(titleElement)
	return tag.text

# Search within a search bar form
def search(browser, url, target, formId=0, formId2=0, subForm=0):
	browser.open(url)
	browser.select_form(nr=formId)
	browser.set_value(target, nr=formId2)
	req = browser.submit(nr=subForm)
	return req.geturl()

# Scrape the image from a webpage with a parameter to remove unwanted images and a specific number of images
def scrapeImages(soupObject, numberOfImgs, numToRemoveFront, PATH, filename):
	images = soupObject.find_all('img')[numToRemoveFront:]

	for i in range(numberOfImgs):
		try:
			url = images[i]['src']
			extension = url.split('/')[-1][-4:-1] + url.split('/')[-1][-1]
			data = requests.get(url).content
			createFile(f'{PATH}{filename}{i+1}{extension}', 'wb', data)
		except: continue
