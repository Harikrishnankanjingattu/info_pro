
CREATE TABLE employees (
 employee_id VARCHAR(10) PRIMARY KEY,
 full_name VARCHAR(100),
 department VARCHAR(50),
 designation VARCHAR(50),
 email VARCHAR(100),
 location VARCHAR(50),
 monthly_salary_inr INT
);

CREATE TABLE products (
 product_id VARCHAR(10) PRIMARY KEY,
 product_name VARCHAR(100),
 category VARCHAR(50),
 launch_year INT,
 annual_revenue_usd INT
);

CREATE TABLE clients (
 client_id VARCHAR(10) PRIMARY KEY,
 client_name VARCHAR(100),
 industry VARCHAR(50),
 country VARCHAR(50),
 annual_contract_value_usd INT
);

CREATE TABLE projects (
 project_id VARCHAR(10) PRIMARY KEY,
 project_name VARCHAR(100),
 product_name VARCHAR(100),
 start_date DATE,
 end_date DATE,
 status VARCHAR(30)
);

CREATE TABLE crm_leads (
 lead_id VARCHAR(10) PRIMARY KEY,
 company_name VARCHAR(100),
 interested_product VARCHAR(100),
 sales_stage VARCHAR(50),
 account_manager VARCHAR(100)
);

CREATE TABLE it_tickets (
 ticket_id VARCHAR(10) PRIMARY KEY,
 product_name VARCHAR(100),
 issue_summary TEXT,
 priority VARCHAR(20),
 status VARCHAR(30)
);

INSERT INTO employees VALUES ('E001','Rohit Kumar 1','Engineering','Senior Engineer','rohit.kumar1@tcs.com','Bengaluru',66200);
INSERT INTO products VALUES ('P001','InsightAI Platform 1','AI Analytics',2019,1245000);
INSERT INTO clients VALUES ('C001','Infosys Client Unit 1','BFSI','India',325000);
INSERT INTO projects VALUES ('PRJ001','Enterprise AI Deployment 1','InsightAI Platform 2','2024-01-15','2025-06-30','Active');
INSERT INTO crm_leads VALUES ('L001','Axis Bank Division 1','InsightAI Platform 2','Prospecting','Rohit Kumar 2');
INSERT INTO it_tickets VALUES ('TCK001','InsightAI Platform 2','Model latency during peak hours','High','Resolved');
