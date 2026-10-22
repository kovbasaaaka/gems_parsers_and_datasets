from bs4 import BeautifulSoup
import requests
from time import sleep
import random
import threading
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from pathlib import Path

output_path = Path(__file__).parent / 'gems_raw.csv'

headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

session = requests.Session()
session.headers.update(headers)

list_gems_data = []
lock = threading.Lock()


def get_url():
    for pages_count in range(1, 49):
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
            link = element.find("a")
            if not link:
                continue
            gem_url = 'https://kolvika.ru' + link.get("href")

            price_tag = element.find("div", class_="product-preview__price-cur product-preview__price-range")
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
    for prop in soup.find_all("div", class_='property'):
        name_tag = prop.find("div", class_='property-name')
        value_tag = prop.find("div", class_='property-content')
        if name_tag and value_tag:
            gems_info[name_tag.get_text(strip=True)] = value_tag.get_text(strip=True)

    with lock:
        list_gems_data.append({
            **gems_info,
            'gem_price': gem_price,
            'gem_url': gem_url,
        })


with ThreadPoolExecutor(max_workers=7) as executor:
    executor.map(parse_gem, get_url())

print(f'Собрано {len(list_gems_data)} записей')

df = pd.DataFrame(list_gems_data)
df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f'Сохранено в {output_path}')