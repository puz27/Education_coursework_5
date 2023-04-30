from src.RequestManager import RequestManager
from src.DBManager import DBManager
from sql.queries import query_create_table_companies, query_create_table_vacancies
from src.utils import config, user_menu


print("Приветствие...")
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

# connection_params = config()
# connector_to_db = DBManager(connection_params, "qwerty")
# print("Делаем запрос к HEAD HUNTER.")
# head_hunter_data = RequestManager()
# companies_list = ["Yandex"]
# head_hunter_data.get_request("Милка")
#
# for company in companies_list:
#     head_hunter_data = RequestManager()
#     head_hunter_data.get_request("Газпром")
#     companies_data, vacancies_data = head_hunter_data.companies_data, head_hunter_data.vacancies_data
#     connector_to_db.insert_data("companies", companies_data)
#     connector_to_db.insert_data("vacancies", vacancies_data)

while True:
    print(*user_menu)
    user_answer = input()

    # End processing
    if user_answer == user_menu["6.Завершить обработку.\n"]:
        break

    # Get_companies_and_vacancies
    elif user_answer == user_menu[" 1.Получить список всех компаний и количество вакансий у каждой компании.\n"]:
        connector_to_db.get_companies_and_vacancies()
        input("Для продолжения нажмите Enter...")

    # Get_all_vacancies
    elif user_answer == user_menu["2.Получить список всех вакансий с информацией.\n"]:
        connector_to_db.get_all_vacancies()
        input("Для продолжения нажмите Enter...")

    # Get_avg_salary
    elif user_answer == user_menu["3.Получить среднюю зарплату по вакансиям.\n"]:
        connector_to_db.get_avg_salary()
        input("Для продолжения нажмите Enter...")

    # Get_vacancies_with_higher_salary
    elif user_answer == user_menu["4.Получить список всех вакансий, у которых зарплата выше средней.\n"]:
        connector_to_db.get_vacancies_with_higher_salary()
        input("Для продолжения нажмите Enter...")

    # Get_vacancies_with_keyword
    elif user_answer == user_menu["5.Получить список всех вакансий, в названии которых содержатся переданные слова.\n"]:
        user_keyword = input()
        connector_to_db.get_vacancies_with_keyword(user_keyword)
        input("Для продолжения нажмите Enter...")

    else:
        print("Некорректный запрос.\n")
