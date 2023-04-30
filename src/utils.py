from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db


user_menu = {
        " 1.Получить список всех компаний и количество вакансий у каждой компании.\n": "1",
        "2.Получить список всех вакансий с информацией.\n": "2",
        "3.Получить среднюю зарплату по вакансиям.\n": "3",
        "4.Получить список всех вакансий, у которых зарплата выше средней.\n": "4",
        "5.Получить список всех вакансий, в названии которых содержатся переданные слова.\n": "5",
        "6.Завершить обработку.\n": "6"
        }