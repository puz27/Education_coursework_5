from configparser import ConfigParser
import psycopg2


def config(filename="database.ini", section="postgresql"):
    """
    Get configuration for connection to database
    :param filename: name of configuration file
    :param section: name of section in configuration file
    :return:
    """
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


def connection_to_db(connection: psycopg2, query_db: str) -> None:
    """
    Connect to database
    :param connection: configuration for connection
    :param query_db: query to database
    :return:
    """
    try:
        with connection:
            with connection.cursor() as cursor:
                query = query_db
                cursor.execute(query)
                connection.commit()
                for company in (cursor.fetchall()):
                    print(*company)
    except psycopg2.Error as er:
        print(f"Ошибка с запросом.\n{er}")
    finally:
        connection.close()


# User menu
user_menu_hh = {
        " 1.Сделать запрос к HEAD HUNTER.\n": "1",
        "2.Не делать запрос к HEAD HUNTER. В БД уже есть данные.\n": "2",
        "3.Кастомный запрос к HEAD HUNTER.\n": "3"
        }


# User query menu
user_menu = {
        " 1.Получить список всех компаний и количество вакансий у каждой компании.\n": "1",
        "2.Получить список всех вакансий с информацией о них.\n": "2",
        "3.Получить среднюю зарплату по вакансиям в разрезе компаний.\n": "3",
        "4.Получить среднюю зарплату по вакансиям.\n": "4",
        "5.Получить список всех вакансий, у которых зарплата выше средней.\n": "5",
        "6.Получить список всех вакансий, в названии которых содержатся переданные слова.\n": "6",
        "7.Завершить обработку.\n": "7"
        }
