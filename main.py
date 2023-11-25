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
            # print(href)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    # for item_name in soup.findAll('h1', {'class': 'ProductMeta__Title Heading u-h2'}):
    # print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://sweatscollective.com" + link.get('href')
        print(href)


store_crawler(1)
