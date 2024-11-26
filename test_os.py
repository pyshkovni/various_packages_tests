# Эксперименты с пакетом os

# C чего мы начинаем изучение новой библиотеки?
# 1. Погуглить/поджипидишить ->  генерация, гайд, страница библиотеки, pypi
# 2. Поиск через pypi.org -> страница библиотеки
# 3. Почитать документацию
# https://docs.python.org/3/library/os.html

 # импорты
import os

def os_tests():

    print("В каком каталоге мы находимся?", os.getcwd())
    # Перейти в каталог,
    os.chdir("data/")
    print("текущий каталог", os.getcwd())
    print("Список текущих файлов", os.listdir())

    # рекурсивный перебор директорий (и вложенных тоже)
    for dirs, files, path in os.walk("."):
        print(dirs)
        print(files)
        print(path)

