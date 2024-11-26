# Эксперименты с библиотекой bs4 и requests

# C чего мы начинаем изучение новой библиотеки?
# 1. Погуглить/поджипидишить ->  генерация, гайд, страница библиотеки, pypi
# 2. Поиск через pypi.org -> страница библиотеки
# 3. Почитать документацию
# bs4
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# requests
# https://requests.readthedocs.io/en/latest/

# https://www.crummy.com/software/BeautifulSoup/

# импорт
import requests
from bs4 import BeautifulSoup

# ссылка для стягивания

def bs4_tests(url):
    # подключение к источнику по http
    response = requests.get(url)

    # статус код 200 - говорит что запрос успешен
    print(response)

    # создание объекта BeautifulSoup для разделения кода страницы на теги
    soup = BeautifulSoup(response.text, "html.parser")

    # что такое тег? https://blog.skillfactory.ru/glossary/teg/
    print(
        soup.title,  # тег вкладки
        soup.title.name,  # название тега
        soup.title.string,  # содержание тега
        soup.title.parent.name,  # имя родительского тега
        soup.p,  # тег параграфа
        soup.p['class'],  # тег с атрибутом
        soup.a,  # тег ссылки
        soup.find_all('a')[:5],  # найти все по тегу 
        soup.find("а")  # найти первый попавшийся тег
        )