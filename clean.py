import pandas as pd

df1 = pd.read_csv('data/raw_data/gems_raw.csv')
df2 = pd.read_csv('data/raw_data/gemstock_raw.csv')

print('-----ИНФОРМАЦИЯ ДО ОЧИСТКИ ПУСТЫХ ЗНАЧЕНИЙ-----')
print('---KOLVIKA INFO---\n')
print(f'{df1.shape}\n')
print(f'{df1.dtypes}\n')
print(f'{df1.isnull().sum()}\n')

print(f'---GEMSTOCK INFO---\n')
print(f'{df2.shape}\n')
print(f'{df2.dtypes}\n')
print(f'{df2.isnull().sum()}\n')

def delete_empty_columns(df1, df2):
    # Удаление столбцов с пустыми значениями из df1 и df2
    df2.drop(['резерв', 'Коллекция', 'Дополнительная вставка', 'Вес изделия', 'Производитель', 'Металл', 'Размер кольца US size', 'Размер кольца Ø', 'GS Index', 'Визуальный размер', 'Бриллиация'], axis=1, inplace=True)
    df1.drop(['Вес', 'Насыщенность камня', 'Вес изделия', 'Вес партии', 'Артикул', 'Качество', 'Цвет', 'Длина А', 'Длина В', 'Длина С'], axis=1, inplace=True)

def delete_unusual_columns(df):
    df.drop(['Изготовим на заказ'], axis=1, inplace=True)

def rename_columns(df1, df2):
    df1.rename(columns={"Название камня": "gem_name", "Вес камня": "gem_weight", "Огранка камня": "gem_cutting", "Облагораживание камня": "gem_enhancement", "Происхождение камня": "gem_origin", "Вид": "gem_view", "Драгоценность камня": "gem_preciousness", "Чистота камня": "gem_clarity", "Форма камня": "gem_form", "Сертификат": "gem_sertificate"}, inplace=True)
    df2.rename(columns={"Масса": "gem_weight", "Чистота": "gem_clarity", "Сертификат": "gem_sertificate", "Происхождение": "gem_origin", "Облагораживание": "gem_enhancement", "Форма огранки": "gem_cutting", "Размеры": "gem_size", "Качество огранки": "gem_cut_quality", "Основной цвет": "gem_main_color", "Цена за камень/за карат": "gem_price", "Комплектность": "gem_completeness", "Наименование камня": "gem_name"}, inplace=True)

delete_empty_columns(df1, df2)
delete_unusual_columns(df2)
rename_columns(df1, df2)

print('-----ИНФОРМАЦИЯ ПОСЛЕ ОЧИСТКИ ПУСТЫХ ЗНАЧЕНИЙ-----\n')
print('---KOLVIKA INFO---\n')
print(f'{df1.shape}\n')
print(f'{df1.dtypes}\n')
print(f'{df1.isnull().sum()}\n')

print(f'---GEMSTOCK INFO---\n')
print(f'{df2.shape}\n')
print(f'{df2.dtypes}\n')
print(f'{df2.isnull().sum()}\n')

df1.to_csv('data/clean_data/kolvika_clean.csv', index=False, encoding='utf-8-sig')
df2.to_csv('data/clean_data/gemstock_clean.csv', index=False, encoding='utf-8-sig')