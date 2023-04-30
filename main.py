from src.RequestManager import RequestManager
from src.DBManager import DBManager
from sql.queries import query_create_table_companies, query_create_table_vacancies

# head_hunter_data = RequestManager()
# head_hunter_data.get_request("Yandex")
# # print(head_hunter_data.companies_data)
# # print(head_hunter_data.vacancies_data)
# companies_data, vacancies_data = head_hunter_data.companies_data, head_hunter_data.vacancies_data
# print(len(companies_data))
# print(len(vacancies_data))




#connector_to_db = DBManager("localhost", "postgres", "123456", "test_base")
# connector_to_db.create_database("test_base")

# connector_to_db.create_table("companies", query_create_table_companies)
# connector_to_db.create_table("vacancies", query_create_table_vacancies)
#
# connector_to_db.insert_data("companies", companies_data)
# connector_to_db.insert_data("vacancies", vacancies_data)

#connector_to_db.get_companies_and_vacancies()
# connector_to_db.get_all_vacancies()
# connector_to_db.get_avg_salary()
#connector_to_db.get_vacancies_with_higher_salary()
#connector_to_db.get_vacancies_with_keyword("Ведущий")

print("Приветствие...")
# user settings
user_host = input("Введите адрес хоста для работы с БД.\n")
user_login = input("Введите логин для работы с БД.\n")
user_psw = input("Введите пароль для работы с БД.\n")

# create/not create base
while True:
    user_base = input("1 - БД уже существует, 2 - создать новую БД\n")
    if user_base == "1":
        print("БД уже есть. Продолжаем.")
        user_base_name = input("Введите имя существующей БД.\n")
        connector_to_db = DBManager(user_host, user_login, user_psw, user_base_name)
        break
    elif user_base == "2":
        user_base_name = input("Введите имя БД.\n")
        print(f"Создаем БД {user_base_name}.")
        connector_to_db = DBManager(user_host, user_login, user_psw, user_base_name)
        connector_to_db.create_database(user_base_name)
        connector_to_db.create_table("companies", query_create_table_companies)
        connector_to_db.create_table("vacancies", query_create_table_vacancies)
        break
    else:
        print("Некорректный ввод.")


print("Делаем запрос к HEAD HUNTER.")
head_hunter_data = RequestManager()
companies_list = ["Yandex"]

for company in companies_list:
    head_hunter_data = RequestManager()
    head_hunter_data.get_request("Yandex")
    companies_data, vacancies_data = head_hunter_data.companies_data, head_hunter_data.vacancies_data
    connector_to_db.insert_data("companies", companies_data)
    connector_to_db.insert_data("vacancies", vacancies_data)
