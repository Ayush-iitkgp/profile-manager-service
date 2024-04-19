customer_id UUID PRIMARY KEY
email VARCHAR(255) UNIQUE NOT NULL
hashed_password TEXT 
country VARCHAR(2) NOT NULL
language VARCHAR(2) CHECK (language IN ('de', 'en')) NOT NULL


CREATE INDEX idx_customers_email ON CUSTOMERS(email);