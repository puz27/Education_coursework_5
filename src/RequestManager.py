import requests
import time
from tqdm import tqdm


class RequestManager:
    """ Class gets data from HEAD HUNTER"""
    def __init__(self):
        self.__companies_data = []
        self.__vacancies_data = []

    @property
    def companies_data(self) -> list:
        return self.__companies_data

    @property
    def vacancies_data(self) -> list:
        return self.__vacancies_data

    def get_request(self, company_name: str) -> None or str:
        """
        Get data from HEAD HUNTER
        :param company_name: filter for search company and vacancies
        :return: list with
        """

        url_company = "https://api.hh.ru/employers"
        url_vacancy = "https://api.hh.ru/vacancies"

        params_company = {
            "text": company_name,
            "only_with_vacancies": "true",
            "per_page": 15,
            "page": 0,
        }

        response = requests.get(url_company, params=params_company)
        if response.status_code == 200:
            all_companies = response.json()["items"]
            for _ in tqdm(range(100), ncols=80, ascii=True, desc='Total'):
                time.sleep(0.01)
            for company in all_companies:

                # Url for vacancies if company
                one_company = (company["id"], company["name"])
                self.__companies_data.append(one_company)

                # Get information about vacancies in company
                employer_id = company["id"]
                page_number = 0
                last_page = 1

                while page_number < last_page:

                    params_vacancy = {
                        "per_page": 100,
                        "employer_id": employer_id,
                        "page": page_number
                    }

                    vacancy_response = requests.get(url_vacancy, params=params_vacancy)
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

                        one_vacancy = (vacancy["id"],
                                       company["id"],
                                       vacancy["name"],
                                       vacancy["url"],
                                       salary_from,
                                       salary_to,
                                       vacancy["area"]["name"])
                        self.__vacancies_data.append(one_vacancy)

                    page_number += 1



        else:
            return "Error:", response.status_code
