from bs4 import BeautifulSoup
import requests
from time import sleep
import random
import threading
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from pathlib import Path

output_path = Path(__file__).parent / 'gems.csv'

headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

session = requests.Session()
session.headers.update(headers)

list_gems_data = []
lock = threading.Lock()


def get_url():
    for pages_count in range(1, 166):
        sleep(random.uniform(1, 3.5))
        url = f'https://gemstock.ru/collection/gems/?page={pages_count}'
        try:
            response = session.get(url, timeout=15)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f'Ошибка на странице {pages_count}: {e}')
            continue

        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all("a", class_="product s-product-wrapper")
        for element in data:
            link = element.get('href')
            if not link:
                continue
            gem_url = 'https://gemstock.ru' + link

            price_tag = element.find("div", class_="price__new")
            gem_price = price_tag.get_text(strip=True) if price_tag else None

            yield gem_url, gem_price

def parse_gem(item):
    gem_url, gem_price = item
    sleep(random.uniform(0.5, 1.5))

    try:
        response = session.get(gem_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Ошибка на {gem_url}: {e}')
        return

    soup = BeautifulSoup(response.text, 'lxml')

    gems_info = {}
    for prop in soup.find_all("div", class_='list__item list__item_dl list__item_default'):
        name_tag = prop.find("div", class_='list__var')
        value_tag = prop.find("div", class_='list__val value')
        if name_tag and value_tag:
            gems_info[name_tag.get_text(strip=True)] = value_tag.get_text(strip=True)
    
    gem_name_tag = soup.find("h1", class_="product-detail__title")
    gem_name_find = gem_name_tag.find("span") if gem_name_tag else None
    gem_name = gem_name_find.get_text() if gem_name_find else None
    
    with lock:
        list_gems_data.append({
            **gems_info,
            'Цена за камень/за карат': gem_price,
            'Ссылка на камень': gem_url,
            'Наименование камня': gem_name,
        })


with ThreadPoolExecutor(max_workers=7) as executor:
    executor.map(parse_gem, get_url())

print(f'Собрано {len(list_gems_data)} записей')

df = pd.DataFrame(list_gems_data)
df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f'Сохранено в {output_path}')