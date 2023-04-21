import requests

url_head_hunter = "https://api.hh.ru/employers"
params = {
    "text": "YES Холдинг",
    "only_with_vacancies": "true",
    "per_page": 10,
    "page": 1,
}

response = requests.get(url_head_hunter, params=params)
print(response)
all_firms = response.json()
print(all_firms)
# for firm in all_firms:
#
#     print("Фирма:", firm["name"])
#     print(firm["id"])
#     firm_id = firm["id"]
#     print("Количество открытых вакансий", firm["open_vacancies"])
#     print(firm["vacancies_url"])
#     firm_id_url = firm["vacancies_url"]

    # vacancy_id_response = requests.get(firm_id_url)
    # vacancies = response.json()["items"]
    #
    # print("\nИнформация по вакансиям предприятия")
    # for vacancy in vacancies:
    #     print(vacancy["id"])
    #     print(vacancy["name"])
    #     print(vacancy["url"])

    #print("------------------------------------------------")



    # url_head_hunter2 = "https://api.hh.ru/vacancies/"
    # params2 = {
    #     "employer_id": firm_id,
    #     "per_page": 10,
    #     "page": 10,
    # }
    #
    # response2 = requests.get(url_head_hunter2, params=params2)
    # z = response2.json()
    # print(z)



