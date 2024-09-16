# Dylan Stitt
# Web Scraping
# U6L4 - Independent Research

from bs4 import BeautifulSoup
from requests_html import HTMLSession

from Scraping import *
import requests

# Const of chars to loop through
CHARS = ['"', '{', '}', '[', ']', '']

# Uses a request_html session to collect the off of the api page I want
def searchCompany(company, url):
	session = HTMLSession()
	response = session.get(url.replace('[stockName]', company))
	soup = BeautifulSoup(response.content, 'html.parser')

	return soup.text

# Cleans the data into what I need
def cleanData(data):
	# Removes those chars from top of file
	for i in CHARS:
		data = data.replace(i, '')

	# Splits the giant list down into the list of info I want
	data = data.split('primaryData:')[1].split(',isRealTime')[0].split(',')

	# Runs the if, if the stock value > $1000
	if len(data) > 6:
		temp = data[0].split(':')
		data[0] = (temp[0]+' : ')+(temp[1]+data[1])
		del data[1]

	# Final cleanup and return cleaned data
	data[0] = '\t'+data[0]
	data[-2] = data[-2]+data[-1]
	del data[-1]
	
	return '\n\t'.join(data)

def main():
	# Urls used
	url = 'https://stockanalysis.com/list/nasdaq-stocks/'
	urlTemplate = 'https://api.nasdaq.com/api/quote/[stockName]/info?assetclass=stocks'

	# Get the page and scrape the companies names and stock names
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	companies = soup.find_all(class_='sym svelte-eurwtr')[1:101]
	names = soup.find_all(class_='slw svelte-eurwtr')[1:101]

	# Run all other functions and write to the file to display the current stock info
	for i in range(len(companies)):
		stockData = searchCompany(companies[i].text, urlTemplate)
		stockData = cleanData(stockData)
		stockData = names[i].text+':\n\n'+stockData+'\n\n'
		createFile('C:/Users/Dylan Stitt/OneDrive/Desktop/Code/Python/Scraping/Lab-4/stocks.txt', 'a', stockData)

# Clears the text file and thens runs main again for new results
if __name__ == '__main__':
	clearFile('C:/Users/Dylan Stitt/OneDrive/Desktop/Code/Python/Scraping/Lab-4/stocks.txt')
	main()
	