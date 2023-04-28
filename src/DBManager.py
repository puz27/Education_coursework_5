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
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass
