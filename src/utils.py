from configparser import ConfigParser
from tqdm import tqdm
from time import sleep


def progress_bar():
   for _ in tqdm(range(100), ncols=80, ascii=True, desc='Total'):
      sleep(0.1)


def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Секция {0} не найдена в {1}.'.format(section, filename))
    return db


user_menu_hh = {
        " 1.Сделать запрос к HEAD HUNTER.\n": "1",
        "2.Не делать запрос к HEAD HUNTER. В БД уже есть данные.\n": "2",
        "3.Кастомный запрос к HEAD HUNTER.\n": "3"
        }


user_menu = {
        " 1.Получить список всех компаний и количество вакансий у каждой компании.\n": "1",
        "2.Получить список всех вакансий с информацией о них.\n": "2",
        "3.Получить среднюю зарплату по вакансиям в разрезе компаний.\n": "3",
        "4.Получить среднюю зарплату по вакансиям.\n": "4",
        "5.Получить список всех вакансий, у которых зарплата выше средней.\n": "5",
        "6.Получить список всех вакансий, в названии которых содержатся переданные слова.\n": "6",
        "7.Завершить обработку.\n": "7"
        }

