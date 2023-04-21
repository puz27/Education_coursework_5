import psycopg2


class DBManager:

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
        database="course",
        user="postgres",
        password="123456"
    )
    try:
        with connection:
            with connection.cursor() as cursor:

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
                connection.commit()
                print(f"Операция над таблицей прошла успешно.")
    except psycopg2.Error:
        print("Ошибка с запросом.")
    finally:
        connection.close()


send_query_create_tables()


