# Create table companies
query_create_table_companies = f"""
                        CREATE TABLE companies (
                        customer_id VARCHAR(20) PRIMARY KEY,
                        company_name VARCHAR(50) NOT NULL,
        	            contact_name VARCHAR(30));
        	            """


# Create table companies
query_create_table_vacancies = """
                CREATE TABLE vacancies (
                customer_id VARCHAR(20) PRIMARY KEY,
                company_name VARCHAR(50) NOT NULL,
                contact_name VARCHAR(30));
                """