import requests


url_head_hunter = "https://api.hh.ru/employers"
params = {
    "text": "газпром",
    "only_with_vacancies": "true",
    "per_page": 10,
    "page": 1,
}

response = requests.get(url_head_hunter, params=params)
print(response)
all_firms = response.json()["items"]
print(all_firms)

for firm in all_firms:

    print("Фирма:", firm["name"])
    print(firm["id"])
    firm_id = firm["id"]
    print("Количество открытых вакансий", firm["open_vacancies"])
    print(firm["vacancies_url"])
    firm_id_url = firm["vacancies_url"]

    vacancy_id_response = requests.get(firm_id_url)
    vacancies = response.json()["items"]
    print(vacancies)
    for vacancy in vacancies:
        print(vacancy["name"])
        print(vacancy["id"])
        print(vacancy["vacancies_url"])
        url_head_hunter = vacancy["vacancies_url"]

        response_vacancy = requests.get(url_head_hunter)
        print(response_vacancy.reason)
        vacancies_in_firm = response_vacancy.json()["items"]

        for vacancy in vacancies_in_firm:
            print(vacancy["id"])
            print(vacancy["name"])
            print(vacancy["salary"])
            print(vacancy["address"])
            print("---------------------------------------")



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



