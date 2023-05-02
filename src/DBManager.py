import psycopg2


class DBManager:
    """ Class connects and works with bases"""
    def __init__(self, connection_params: dict, database=None):
        self.__database = database
        self.__connection_params = connection_params

    def create_database(self, new_database: str) -> None:
        """
        Create new database
        :param new_database:  name of new database
        :return:
        """
        self.__connection_params.update({'dbname': "postgres"})
        connection = psycopg2.connect(**self.__connection_params)
        connection.autocommit = True

        try:
            with connection.cursor() as cursor:
                query_create_base = f"CREATE DATABASE {new_database}"
                cursor.execute(query_create_base)
                self.__database = new_database
                print(f"База данных {new_database} успешно создана.")
        except psycopg2.Error as er:
            print(f"БД:{new_database}. Ошибка с запросом создания БД.\n{er}")
        finally:
            connection.close()

    def create_table(self, table_name: str, query: str) -> None:
        """
        Create new table
        :param table_name: name of table
        :param query: query for creation table
        :return:
        """
        self.__connection_params.update({'dbname': self.__database})
        connection = psycopg2.connect(**self.__connection_params)

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
        """
        Insert new data to database
        :param table: table name for insert
        :param data: list with data for processing
        :return:
        """
        self.__connection_params.update({'dbname': self.__database})
        connection = psycopg2.connect(**self.__connection_params)

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

    def get_companies_and_vacancies(self) -> None:
        """
        Get all companies and vacancies count from database
        :return:
        """
        self.__connection_params.update({'dbname': self.__database})
        connection = psycopg2.connect(**self.__connection_params)

        try:
            with connection:
                with connection.cursor() as cursor:
                    query = f"""select companies.company_name, COUNT(*) from companies
                    INNER JOIN vacancies USING (company_id)
                    GROUP BY company_name"""
                    cursor.execute(query)
                    connection.commit()
                    for company in (cursor.fetchall()):
                        print(*company)
        except psycopg2.Error as er:
            print(f"Ошибка с запросом.\n{er}")
        finally:
            connection.close()

    def get_all_vacancies(self):
        """
        Get all vacancies from database
        :return:
        """
        self.__connection_params.update({'dbname': self.__database})
        connection = psycopg2.connect(**self.__connection_params)

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

    def get_avg_salary_by_company(self) -> None:
        """
        Get average salary for companies from database
        :return:
        """
        self.__connection_params.update({'dbname': self.__database})
        connection = psycopg2.connect(**self.__connection_params)

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

    def get_avg_salary(self) -> None:
        """
        Get average salary from all vacancies from database
        :return:
        """
        self.__connection_params.update({'dbname': self.__database})
        connection = psycopg2.connect(**self.__connection_params)

        try:
            with connection:
                with connection.cursor() as cursor:
                    query = f"""
                    SELECT AVG(vacancy_salary_from)::numeric(10,0) FROM vacancies
                    """
                    cursor.execute(query)
                    connection.commit()
                    for vacancy in (cursor.fetchall()):
                        print(*vacancy)
        except psycopg2.Error as er:
            print(f"Ошибка с запросом.\n{er}")
        finally:
            connection.close()

    def get_vacancies_with_higher_salary(self) -> None:
        """
        Get vacancies with bigger salary than average salary from database
        :return:
        """
        self.__connection_params.update({'dbname': self.__database})
        connection = psycopg2.connect(**self.__connection_params)

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

    def get_vacancies_with_keyword(self, search_word: str) -> None:
        """
        Get vacancies that need find from database
        :param search_word: search filter
        :return:
        """
        self.__connection_params.update({'dbname': self.__database})
        connection = psycopg2.connect(**self.__connection_params)

        try:
            with connection:
                with connection.cursor() as cursor:
                    query = f"""
                    SELECT * FROM vacancies
                    WHERE vacancy_name LIKE '%{search_word}%'
                    """
                    cursor.execute(query)
                    connection.commit()
                    for vacancy in (cursor.fetchall()):
                        print(*vacancy)
        except psycopg2.Error as er:
            print(f"Ошибка с запросом.\n{er}")
        finally:
            connection.close()
