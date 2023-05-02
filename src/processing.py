import tqdm
from src.RequestManager import RequestManager
from src.DBManager import DBManager
from sql.queries import query_create_table_companies, query_create_table_vacancies
from src.utils import config, user_menu_hh, user_menu


def main_processing():
    # user settings
    connection_params = config()

    # create/not create base
    while True:
        user_base = input("1 - БД уже существует, 2 - создать новую БД\n")
        if user_base == "1":
            print("БД уже есть. Продолжаем.")
            user_base_name = input("Введите имя существующей БД.\n")
            connector_to_db = DBManager(connection_params, user_base_name)
            break
        elif user_base == "2":
            user_base_name = input("Введите имя БД.\n")
            print(f"Создаем БД {user_base_name}.")
            connector_to_db = DBManager(connection_params, user_base_name)
            connector_to_db.create_database(user_base_name)
            connector_to_db.create_table("companies", query_create_table_companies)
            connector_to_db.create_table("vacancies", query_create_table_vacancies)
            break
        else:
            print("Некорректный ввод.")

    # request to HEAD HUNTER
    head_hunter_data = RequestManager()
    while True:

        print(*user_menu_hh)
        user_answer_hh = input()

        # Request to HEAD HUNTER
        if user_answer_hh == user_menu_hh[" 1.Сделать запрос к HEAD HUNTER.\n"]:

            all_companies = ["Газпром", "Yandex", "МТС", "ПИК", "Ланит"]
            for company in all_companies:
                print(f"Обрабатываем {company}.")
                head_hunter_data.get_request(company)
            companies_data, vacancies_data = head_hunter_data.companies_data, head_hunter_data.vacancies_data
            connector_to_db.insert_data("companies", companies_data)
            connector_to_db.insert_data("vacancies", vacancies_data)
            input("\nЗапрос выполнен. Для продолжения нажмите Enter...\n")
            break

        # Custom request to HEAD HUNTER
        elif user_answer_hh == user_menu_hh["3.Кастомный запрос к HEAD HUNTER.\n"]:

            user_query = input("Введите название компании.\n")
            head_hunter_data.get_request(user_query)
            companies_data, vacancies_data = head_hunter_data.companies_data, head_hunter_data.vacancies_data
            connector_to_db.insert_data("companies", companies_data)
            connector_to_db.insert_data("vacancies", vacancies_data)
            input("\nЗапрос выполнен. Для продолжения нажмите Enter...\n")
            break

        # No request
        elif user_answer_hh == user_menu_hh["2.Не делать запрос к HEAD HUNTER. В БД уже есть данные.\n"]:
            break

        else:
            print("Некорректный запрос.\n")

    # Query to base
    while True:
        print()
        print(*user_menu)
        user_answer = input()

        # End processing
        if user_answer == user_menu["7.Завершить обработку.\n"]:
            break

        # Get_companies_and_vacancies
        elif user_answer == user_menu[" 1.Получить список всех компаний и количество вакансий у каждой компании.\n"]:
            connector_to_db.get_companies_and_vacancies()
            input("Для продолжения нажмите Enter...")

        # Get_all_vacancies
        elif user_answer == user_menu["2.Получить список всех вакансий с информацией о них.\n"]:
            connector_to_db.get_all_vacancies()
            input("Для продолжения нажмите Enter...\n")

        # Get_avg_salary_by_company
        elif user_answer == user_menu["3.Получить среднюю зарплату по вакансиям в разрезе компаний.\n"]:
            input("Расчет идет по 'Зарплата от'. Если данных нет, то результат не включен в выборку.\n"
                  "Для продолжения нажмите Enter...\n")
            connector_to_db.get_avg_salary_by_company()
            input("Для продолжения нажмите Enter...\n")

        # Get_avg_salary
        elif user_answer == user_menu["4.Получить среднюю зарплату по вакансиям.\n"]:
            input("Расчет идет по 'Зарплата от'. Если данных нет, то результат не включен в выборку.\n"
                  "Для продолжения нажмите Enter...\n")
            connector_to_db.get_avg_salary()
            input("Для продолжения нажмите Enter...\n")

        # Get_vacancies_with_higher_salary
        elif user_answer == user_menu["5.Получить список всех вакансий, у которых зарплата выше средней.\n"]:
            connector_to_db.get_vacancies_with_higher_salary()
            input("Для продолжения нажмите Enter...\n")

        # Get_vacancies_with_keyword
        elif user_answer == user_menu["6.Получить список всех вакансий, в названии которых содержатся переданные слова.\n"]:
            user_keyword = input("Введите слово для поиска.\n")
            connector_to_db.get_vacancies_with_keyword(user_keyword)
            input("Для продолжения нажмите Enter...\n")

        else:
            print("Некорректный запрос.\n")