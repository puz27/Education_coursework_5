import psycopg2
from sql.queries import query_create_table_companies, query_create_table_vacancies

class DBManager:

    def __init__(self, host: str, user: str, password: str):
        self.__host = host
        self.__user = user
        self.__password = password
        self.database = None

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
                self.database = database
                print(f"База данных {database} успешно создана.")

        except psycopg2.Error:
            print(f"БД:{database}. Ошибка с запросом создания БД.")
        finally:
            connection.close()

    def create_table(self, table_name: str, query: str):

        connection = psycopg2.connect(
            host=self.__host,
            database=self.database,
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
        except psycopg2.Error:
            print(f"Ошибка с запросом при создании таблицы {table_name}.")
        finally:
            connection.close()

    def get_companies_and_vacancies(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass

def send_query_create_tables() -> None:
    """
    Send SQL queries to Data Base north on localhost
    :param table: Name of table in database.
    :param args: List of data for adding.
    :param user: User name connection.
    :param password: Password user for connection.
    """
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123456"
    )

    # Create database
    connection.autocommit = True
    try:
        with connection.cursor() as cursor:
            query_create_base = "CREATE DATABASE companies_information"
            cursor.execute(query_create_base)
            print("База данных успешно создана")
        connection.close()
    except psycopg2.Error:
        print("Ошибка с запросом создания БД.")
    finally:
        connection.close()



    connection2 = psycopg2.connect(
        host="localhost",
        database="companies_information",
        user="postgres",
        password="123456"
    )

    try:
        with connection2:
            with connection2.cursor() as cursor:

                query_company = """
                CREATE TABLE companies(
                customer_id VARCHAR(20) PRIMARY KEY,
                company_name VARCHAR(50) NOT NULL,
	            contact_name VARCHAR(30));
	            """

                query_vacancies = """
                CREATE TABLE vacancies (
                customer_id VARCHAR(20) PRIMARY KEY,
                company_name VARCHAR(50) NOT NULL,
                contact_name VARCHAR(30));
                """

                cursor.execute(query_company)
                cursor.execute(query_vacancies)
                connection2.commit()
                print(f"Операция над таблицей прошла успешно.")
    except psycopg2.Error:
        print("Ошибка с запросом.")
    finally:
        connection2.close()


#send_query_create_tables()
x = DBManager("localhost", "postgres", "123456")
x.create_database("test")
x.create_table("table_1", query_create_table_vacancies)
x.create_table("table_2", query_create_table_companies)
