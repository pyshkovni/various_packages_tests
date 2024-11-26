# main - стартовый модуль проекта

# импорты из модуля
# from functions import func1, func2
from test_python_docx import python_docx_tests

# функция запуска импортированных функций
def main():
    python_docx_tests("data/Заголовок.docx")

# инициализационный скрипт
if __name__ == '__main__':
    main()
