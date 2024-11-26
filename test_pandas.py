# Эксперименты с библиотекой pandas

# C чего мы начинаем изучение новой библиотеки?
# 1. Погуглить/поджипидишить ->  генерация, гайд, страница библиотеки, pypi
# 2. Поиск через pypi.org -> страница библиотеки
# 3. Почитать документацию
# https://pandas.pydata.org/

# импорт
import pandas as pd

def pandas_tests(path):
    # создание объекта таблицы DataFrame
    df = pd.DataFrame(
        {
            "Name": ["Braund, Mr. Owen Harris","Allen, Mr. William Henry","Bonnell, Miss. Elizabeth",],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )

    # показать таблицу
    print(df)
    # показать колонку
    print(df["Age"])


    # Загрузка данных
    table = pd.read_excel(path)
    print(table)

    # добавление новых колонок
    table["c"] = (table["a"] + table["b"]) * 2
    print(table)

    # можно перебрать как массив
    for i in table["c"]:
        print("Элемент:", i)