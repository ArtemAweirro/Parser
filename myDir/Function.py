from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # для игнорирования SSL-ошибок

def parse():
    url = 'https://omgtu.ru/ecab/persons/index.php?b=16' # передаем необходимый URL адрес
    page = requests.get(url, verify=False) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ

    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    block = soup.findAll('div', style='padding: 5px; font-size: 120%;') # находим  контейнер с нужным классом
    description = ''
    file = open('SikhvartAA_3.txt', 'w', encoding='UTF-8')
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег <a>
            description += data.text.strip() + '\n' # записываем в переменную содержание тега
    print(description) # вывод результата в консоль
    file.write(description) # запись результата в файл
    file.close()
