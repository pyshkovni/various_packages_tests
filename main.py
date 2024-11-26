# main - стартовый модуль проекта

# импорты из модуля
# from functions import func1, func2
from test_python_docx import python_docx_tests
from test_pandas import pandas_tests
from test_os import os_tests

# функция запуска импортированных функций
def main():
    print("----- Тесты python-docs -----")
    python_docx_tests("data/Заголовок.docx")
    print("----- Тесты pandas -----")
    pandas_tests("data/ab.xlsx")
    print("----- Тесты os -----")
    os_tests()

# инициализационный скрипт
if __name__ == '__main__':
    main()
