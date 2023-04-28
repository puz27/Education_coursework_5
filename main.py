from src.RequestManager import RequestManager
from src.DBManager import DBManager
from sql.queries import query_create_table_companies, query_create_table_vacancies

# head_hunter_data = RequestManager()
# head_hunter_data.get_request("Газпром")
# print(head_hunter_data.companies_data)
# print(head_hunter_data.vacancies_data)
# companies_data, vacancies_data = head_hunter_data.companies_data, head_hunter_data.vacancies_data

connector_to_db = DBManager("localhost", "postgres", "123456", "test_base")
#connector_to_db.create_database("test_base")

# connector_to_db.create_table("companies", query_create_table_companies)
# connector_to_db.create_table("vacancies", query_create_table_vacancies)

# connector_to_db.insert_data("companies", companies_data)
# connector_to_db.insert_data("vacancies", vacancies_data)

connector_to_db.get_companies_and_vacancies()







# import requests
#
#
# url_head_hunter = "https://api.hh.ru/employers"
# params = {
#     "text": "газпром",
#     "only_with_vacancies": "true",
#     "per_page": 1,
#     "page": 1,
# }
#
# response = requests.get(url_head_hunter, params=params)
# all_companies = response.json()["items"]
#
# companies_data = []
# vacancies_data = []
#
# for company in all_companies:
#     # print("Фирма:", firm["name"])
#     # print("ID:", firm["id"])
#     company_id = company["id"]
#     # print("Количество открытых вакансий", firm["open_vacancies"])
#     # print(firm["vacancies_url"])
#
#     # Url for vacancies if company
#     company_id_url = company["vacancies_url"]
#
#     # Add all companies (ID, Description, counts of vacancies) to list
#     one_company = (company["id"], company["name"], company["open_vacancies"])
#     companies_data.append(one_company)
#
#     # Get information about vacancies in company
#     vacancy_response = requests.get(company_id_url)
#     vacancies_of_company = vacancy_response.json()["items"]
#
#     for vacancy in vacancies_of_company:
#         # print(vacancy["id"])
#         # print("ID Фирмы:", firm["id"])
#         # print("Название вакансии", vacancy["name"])
#         # print(vacancy["salary"])
#         # print(vacancy["address"])
#         #
#         #print("---------------------------------------")
#
#         # Add all vacancies of company  to list
#
#         if vacancy["salary"]["from"] is not None:
#             salary_from = int(vacancy["salary"]["from"])
#         else:
#             salary_from = 0
#
#         if vacancy["salary"]["to"] is not None:
#             salary_to = int(vacancy["salary"]["to"])
#         else:
#             salary_to = 0
#
#         one_vacancy = (int(vacancy["id"]), int(company["id"]), vacancy["name"], salary_from, salary_to,  vacancy["address"]["city"])
#         vacancies_data.append(one_vacancy)
#
# # print(companies_data)
# print(vacancies_data)

