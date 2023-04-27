# Create table companies
query_create_table_companies = f"""
                        CREATE TABLE companies (
                        company_id SERIAL PRIMARY KEY,
                        company_name VARCHAR(50) NOT NULL,
        	            vacancies_count INT);
        	            """


# Create table companies
query_create_table_vacancies = """
                CREATE TABLE vacancies (
                vacancy_id SERIAL PRIMARY KEY,
                company_id INTEGER REFERENCES companies (company_id),
                vacancy_name VARCHAR(100) NOT NULL,
                vacancy_salary_from INT,
                vacancy_salary_to INT,
                vacancy_address VARCHAR(100));
                """