import requests
from bs4 import BeautifulSoup
from Scraping import *

def main():
    links = [
        'https://www.geeksforgeeks.org/introduction-of-object-oriented-programming/?ref=header_search',
        'https://www.geeksforgeeks.org/introduction-to-algorithms/',
        'https://www.geeksforgeeks.org/data-structures/'
    ]

    for link in links:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        title = scrapeTitle(soup, 'article', 'h1')

        if links.index(link) == 2: results = scrapeId(soup, 'primary')
        else: results = scrapeClass(soup, 'a-wrapper')
        
        createFile(title.replace('|', ''), results)

if __name__ == '__main__':
    main()
