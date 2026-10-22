import pandas as pd

df2 = pd.read_csv('gemstock_raw.csv')

explore_dataframe = df2.sample(n=500, random_state=None) # возвращает случайно собранный из датафрейма набор данных

def dataframe_info(explore_dataframe):
    size = explore_dataframe.shape # .shape возвращает размеры датафрейма в виде: (кол-во строк, кол-во столбцов)
    types_of_data = explore_dataframe.dtypes # .dtypes возвращает типы данных для каждой строки в датафрейме
    print(f"\nРазмеры датафрейма для обучения: {size}\n")
    print(f"Типы данных в датафрейме:\n\n{types_of_data}\n")
    #print(f"Выбор столбцов по типу данных integer:\n{explore_dataframe.select_dtypes(include="int64")}")
    #print(f"Выбор столбцов по типу данных float:\n{explore_dataframe.select_dtypes(include="float64")}")
    #print(f"Выбор столбцов по типу данных object:\n{explore_dataframe.select_dtypes(include="object")}")
    #print(f"Столбец 'Масса':\n{explore_dataframe['Масса'].head(5)}\n")
    #print(f"Столбец 'Наименование камня':\n{explore_dataframe['Наименование камня'].head(5)}\n")
    #print(f"Столбец 'Цена за камень/за карат':\n{explore_dataframe['Цена за камень/за карат'].head(5)}\n")
    #print(f"Столбец 'Форма огранки':\n{explore_dataframe['Форма огранки'].head(5)}\n")
    price_in_int = explore_dataframe['Цена за камень/за карат'].head(5)
    
dataframe_info(explore_dataframe)