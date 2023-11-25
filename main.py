import requests
from bs4 import BeautifulSoup


def store_crawler(maxPages):
    page = 1
    while page <= maxPages:
        url = "https://sweatscollective.com/collections/shop-all?page=" + str(page)
        source_code = requests.get(url)
        source_text = source_code.text
        soup = BeautifulSoup(source_text, "html.parser")
        for link in soup.findAll('a', {'class': 'ProductItem__ImageWrapper'}):
            href = "https://sweatscollective.com" + link.get('href')
            print(href)
        page += 1


store_crawler(1)
