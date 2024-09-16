# Dylan Stitt
# Web Scraping
# Searching

from bs4 import BeautifulSoup
from Scraping import *
import mechanize, requests

def main():
	words = readFile('C:/Users/Dylan Stitt/OneDrive/Desktop/Code/Python/Scraping/Lab-2/key_terms.txt', 'list')
	url = 'https://citizendium.org'
	allContent = {}

	for word in words:
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		new_url = search(browser, url, word, subForm=1)

		page = requests.get(new_url)
		soup = BeautifulSoup(page.content, 'html.parser')

		content = scrapeTag(soup, 'p')
		allContent[word] = content[0].text

	createFile('C:/Users/Dylan Stitt/OneDrive/Desktop/Code/Python/Scraping/Lab-2/words_defined.txt', 'w', allContent)

if __name__ == '__main__':
	main()
