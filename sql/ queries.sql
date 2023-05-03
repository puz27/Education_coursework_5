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

---
--- Get all companies and vacancies count from database
---

select company_name, COUNT(*) from companies
INNER JOIN vacancies USING (company_id)
GROUP BY company_name
ORDER BY company_name;

---
--- Get all vacancies from database
---

select company_name, vacancy_name,
vacancy_salary_from, vacancy_salary_to, vacancy_url  from vacancies
INNER JOIN companies USING (company_id)
ORDER BY company_name;

---
--- Get average salary for companies from database
---

SELECT company_name, AVG(vacancy_salary_from)::numeric(10,0) AS average_salary FROM companies
INNER JOIN vacancies USING (company_id) WHERE vacancy_salary_from <> 0
GROUP BY company_name
ORDER BY average_salary DESC;

---
--- Get average salary from all vacancies from database
---

SELECT AVG(vacancy_salary_from)::numeric(10,0) FROM vacancies;

---
--- Get average salary from all vacancies from database
---

SELECT vacancy_name, vacancy_salary_from FROM vacancies
WHERE vacancies.vacancy_salary_from <> 0 AND vacancy_salary_from > (SELECT AVG(vacancy_salary_from) FROM vacancies)
ORDER BY vacancy_salary_from DESC;

---
--- Get vacancies that need find from database
---

SELECT * FROM vacancies
WHERE vacancy_name LIKE '%{search_word}%';
