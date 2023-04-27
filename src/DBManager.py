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
                    print(*cursor.fetchall())
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
x = DBManager("localhost", "postgres", "123456", "cource")

# x.create_database("cource")
# x.create_table("companies", query_create_table_companies)
#x.create_table("vacancies", query_create_table_vacancies)
# data = [(4565267, "test_test", 10)]
data2 = [(79478667, 4565267, 'Главный специалист отдела', 123, 12345, 'Новомосковский административный округ')]
#
# #x.insert_data("companies", data)
x.insert_data("vacancies", data2)
# x.get_companies_and_vacancies()
