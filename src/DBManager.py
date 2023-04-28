import psycopg2
from sql.queries import query_create_table_companies, query_create_table_vacancies


class DBManager:

    def __init__(self, host: str, user: str, password: str, database=None):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def create_database(self, database: str):

        connection = psycopg2.connect(
            host=self.__host,
            database="postgres",
            user=self.__user,
            password=self.__password
            )

        connection.autocommit = True
        try:
            with connection.cursor() as cursor:
                query_create_base = f"CREATE DATABASE {database}"
                cursor.execute(query_create_base)
                self.__database = database
                print(f"База данных {database} успешно создана.")

        except psycopg2.Error as er:
            print(f"БД:{database}. Ошибка с запросом создания БД.\n{er}")
        finally:
            connection.close()

    def create_table(self, table_name: str, query: str):

        connection = psycopg2.connect(
            host=self.__host,
            database=self.__database,
            user=self.__user,
            password=self.__password
        )

        try:
            with connection:
                with connection.cursor() as cursor:
                    query_create_table = query

                    cursor.execute(query_create_table)
                    connection.commit()
                    print(f"Создание таблицы {table_name} прошло успешно.")
        except psycopg2.Error as er:
            print(f"Ошибка с запросом при создании таблицы {table_name}.\n{er}")
        finally:
            connection.close()

    def insert_data(self, table: str, data: list) -> None:
        connection = psycopg2.connect(
            host=self.__host,
            database=self.__database,
            user=self.__user,
            password=self.__password
        )
        try:
            with connection:
                with connection.cursor() as cursor:
                    col_count = "".join("%s," * len(data[0]))
                    query = f"INSERT INTO {table} VALUES ({col_count[:-1]})"
                    cursor.executemany(query, data)
                    connection.commit()
                    print(f"Операция над таблицей {table} прошла успешно.")
        except psycopg2.Error as er:
            print(f"Ошибка с запросом.\n{er}")
        finally:
            connection.close()

    def get_companies_and_vacancies(self):
        # SELECT  company_name, vacancies_count from companies
        connection = psycopg2.connect(
            host=self.__host,
            database=self.__database,
            user=self.__user,
            password=self.__password
        )
        try:
            with connection:
                with connection.cursor() as cursor:
                    query = f"SELECT  company_name, vacancies_count from companies"
                    cursor.execute(query)
                    connection.commit()
                    for company in (cursor.fetchall()):
                        print(*company)
        except psycopg2.Error as er:
            print(f"Ошибка с запросом.\n{er}")
        finally:
            connection.close()

    def get_all_vacancies(self):
        # select companies.company_name, vacancy_name, vacancy_salary_from, vacancy_salary_to,
        # vacancy_url  from vacancies INNER JOIN companies USING (company_id)
        connection = psycopg2.connect(
            host=self.__host,
            database=self.__database,
            user=self.__user,
            password=self.__password
        )
        try:
            with connection:
                with connection.cursor() as cursor:
                    query = f"""
                    select companies.company_name, vacancy_name,
                    vacancy_salary_from, vacancy_salary_to, vacancy_url  from vacancies
                    INNER JOIN companies USING (company_id)"""
                    cursor.execute(query)
                    connection.commit()
                    for vacancy in (cursor.fetchall()):
                        print(*vacancy)
        except psycopg2.Error as er:
            print(f"Ошибка с запросом.\n{er}")
        finally:
            connection.close()

    def get_avg_salary(self):
        # select companies.company_name, AVG(vacancies.vacancy_salary_from) as average_salry from companies
        # INNER JOIN vacancies USING (company_id) where vacancies.vacancy_salary_from <> 0
        # GROUP BY company_name
        connection = psycopg2.connect(
            host=self.__host,
            database=self.__database,
            user=self.__user,
            password=self.__password
        )
        try:
            with connection:
                with connection.cursor() as cursor:
                    query = f"""
                    SELECT companies.company_name, AVG(vacancies.vacancy_salary_from)::numeric(10,0)  AS average_salary FROM companies
                    INNER JOIN vacancies USING (company_id) WHERE vacancies.vacancy_salary_from <> 0
                    GROUP BY company_name"""
                    cursor.execute(query)
                    connection.commit()
                    for vacancy in (cursor.fetchall()):
                        print(*vacancy)
        except psycopg2.Error as er:
            print(f"Ошибка с запросом.\n{er}")
        finally:
            connection.close()

    def get_vacancies_with_higher_salary(self):
        #select vacancy_name, vacancy_salary_from from vacancies
        #where vacancies.vacancy_salary_from <> 0 and vacancy_salary_from > (select AVG(vacancy_salary_from) from vacancies)
        connection = psycopg2.connect(
            host=self.__host,
            database=self.__database,
            user=self.__user,
            password=self.__password
        )
        try:
            with connection:
                with connection.cursor() as cursor:
                    query = f"""
                    SELECT vacancy_name, vacancy_salary_from FROM vacancies
                    WHERE vacancies.vacancy_salary_from <> 0 AND vacancy_salary_from > (SELECT AVG(vacancy_salary_from) FROM vacancies)
                    ORDER BY vacancy_salary_from DESC
                    """
                    cursor.execute(query)
                    connection.commit()
                    for vacancy in (cursor.fetchall()):
                        print(*vacancy)
        except psycopg2.Error as er:
            print(f"Ошибка с запросом.\n{er}")
        finally:
            connection.close()

    def get_vacancies_with_keyword(self):
        pass
