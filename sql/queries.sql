---
--- Create tables companies and vacancies
---

CREATE TABLE companies (
company_id SERIAL PRIMARY KEY,
company_name VARCHAR(100) NOT NULL
);

CREATE TABLE vacancies (
vacancy_id SERIAL PRIMARY KEY,
company_id INTEGER REFERENCES companies (company_id) ON DELETE CASCADE,
vacancy_name VARCHAR(100) NOT NULL,
vacancy_url VARCHAR(100) NOT NULL,
vacancy_salary_from INT,
vacancy_salary_to INT,
vacancy_address VARCHAR(100),
CONSTRAINT chk_salary_from CHECK(vacancy_salary_from >= 0),
CONSTRAINT chk_salary_to CHECK(vacancy_salary_to >= 0)
);
