# Парсеры и датасеты камней

## Что это
Два парсера для сбора данных о драгоценных и полудрагоценных камнях с сайтов:
- kolvika.ru — ювелирные вставки
- gemstock.ru — огранённые камни

## Результат
- gems_raw.csv — 1502 записи с kolvika
- gemstock_raw.csv — 5928 записей с gemstock
- Итого: ~7400 записей

## Стек
- Python 3
- requests, BeautifulSoup4, lxml
- pandas, ThreadPoolExecutor
- Git

## Что дальше
- Очистка данных
- EDA
- Модель предсказания цены