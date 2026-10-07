from bs4 import BeautifulSoup
import requests
import random
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

session = requests.Session()
session.headers.update(headers)

def get_url():
    for pages_count in range(1, 2):
        sleep(random.uniform(1, 4))

        url = f'https://kolvika.ru/collection/yuvelirnye-vstavki?page={pages_count}'

        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f'Ошибка на странице {pages_count}: {e}')
            continue

        soup = BeautifulSoup(response.text, 'lxml') 

        data = soup.find_all("div", class_="product-preview__content")
        for element in data:
            gem_url = 'https://kolvika.ru' + element.find("a").get("href")
            yield gem_url

url = get_url()
def parse_gem(url):
    sleep(0.5)
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Ошибка на {url}: {e}')
        return
    
    soup = BeautifulSoup(response.text, 'lxml')

    gem_price = soup.find("span", class_="product__buy")
    return f"Цена на камень: {gem_price}"

print(parse_gem(url))