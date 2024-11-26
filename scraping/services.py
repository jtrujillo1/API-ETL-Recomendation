import requests
from bs4 import BeautifulSoup

def scrape_mercadolibre(query):
    url = f"https://listado.mercadolibre.com.co/{query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for item in soup.select('.ui-search-result'):
        title = item.select_one('.ui-search-item__title').text
        price = item.select_one('.price-tag-fraction').text
        link = item.select_one('a')['href']
        image = item.select_one('.ui-search-result-image img')['src']
        results.append({'title': title, 'price': price, 'url': link, 'image': image})

    return results
