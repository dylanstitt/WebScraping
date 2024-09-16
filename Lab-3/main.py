# Dylan Stitt
# Image Scraping
# 5/9/24

from bs4 import BeautifulSoup
from Scraping import *
import requests

def main():
	PATH = "C:/Users/Dylan Stitt/OneDrive/Desktop/Code/Python/Scraping/Lab-3/animal_pics/"
	URL = 'https://stock.adobe.com/search?k=dog&search_type=usertyped'

	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	scrapeImages(soup, 10, 3, PATH, 'dog')

if __name__ == '__main__':
	main()
