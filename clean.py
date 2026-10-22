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

delete_empty_columns(df1, df2)
delete_unusual_columns(df2)
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