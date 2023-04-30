import requests


class RequestManager:

    def __init__(self):
        self.companies_data = []
        self.vacancies_data = []

    def get_request(self, company_name: str):

        url_head_hunter = "https://api.hh.ru/employers"
        params = {
            "text": company_name,
            "only_with_vacancies": "true",
            "per_page": 50,
            "page": 0,
        }

        response = requests.get(url_head_hunter, params=params)
        all_companies = response.json()["items"]

        for company in all_companies:
            # Url for vacancies if company
            company_id_url = company["vacancies_url"]
            print(company_id_url)

            # Add all companies (ID, Description, counts of vacancies) to list
            one_company = (company["id"],
                           company["name"])
            self.companies_data.append(one_company)

            # Get information about vacancies in company
            page_number = 0
            params2 = {
                "per_page": 50,
                "page": page_number,
            }

            vacancy_response = requests.get(company_id_url, params=params2)
            vacancies_of_company = vacancy_response.json()["items"]


            for vacancy in vacancies_of_company:

                if vacancy["salary"] is None:
                    salary_from = 0
                    salary_to = 0
                else:
                    if vacancy["salary"]["from"] is not None:
                        salary_from = int(vacancy["salary"]["from"])
                    else:
                        salary_from = 0

                    if vacancy["salary"]["to"] is not None:
                        salary_to = int(vacancy["salary"]["to"])
                    else:
                        salary_to = 0
                # print(vacancy)
                one_vacancy = (vacancy["id"],
                               company["id"],
                               vacancy["name"],
                               vacancy["url"],
                               salary_from,
                               salary_to,
                               vacancy["area"]["name"])
                self.vacancies_data.append(one_vacancy)

