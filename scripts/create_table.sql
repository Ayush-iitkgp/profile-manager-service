CREATE TABLE customer (
    customer_id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL, -- are we sure that the email will be unique?
    hashed_password TEXT,
    country VARCHAR(2) NOT NULL,
    language VARCHAR(2) CHECK (language IN ('de', 'en')) -- language can be null as see in the data
    -- also language as be something other than de and en and see in the data. these is a record wioth language as ja
);


CREATE INDEX idx_customers_email ON customer(email);

SELECT COUNT(*) from customer;

-- SELECT * from customer where email='osefhhchnsic@protonmail.com';