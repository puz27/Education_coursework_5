import requests


url_head_hunter = "https://api.hh.ru/employers"
params = {
    "text": "газпром",
    "only_with_vacancies": "true",
    #"per_page": 10,
    "page": 1,
}

response = requests.get(url_head_hunter, params=params)
all_firms = response.json()["items"]

companies_data = []
vacancies_data = []

for firm in all_firms:
    # print("Фирма:", firm["name"])
    # print("ID:", firm["id"])
    firm_id = firm["id"]
    # print("Количество открытых вакансий", firm["open_vacancies"])
    # print(firm["vacancies_url"])

    # Url for vacancies if company
    firm_id_url = firm["vacancies_url"]

    # Add all companies (ID, Description, counts of vacancies) to list
    one_company = (firm["id"], firm["name"], firm["open_vacancies"])
    companies_data.append(one_company)

    # Get information about vacancies in company
    vacancy_response = requests.get(firm_id_url)
    vacancies_of_company = vacancy_response.json()["items"]

    for vacancy in vacancies_of_company:
        # print(vacancy["id"])
        # print("ID Фирмы:", firm["id"])
        # print("Название вакансии", vacancy["name"])
        # print(vacancy["salary"])
        # print(vacancy["address"])
        #
        #print("---------------------------------------")

        # Add all vacancies of company  to list
        one_vacancy = (vacancy["id"], firm["id"], vacancy["name"], vacancy["salary"], vacancy["address"])
        vacancies_data.append(one_vacancy)

# print(companies_data)
print(vacancies_data)
    # print("---------------------------------------")
    # print(vacancies_data)
