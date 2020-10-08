-- 1. create offices table, copy this query and paste it
CREATE TABLE IF not EXISTS classicmodels.offices (
  officeCode        varchar(10) NOT NULL,
  city              varchar(50) NOT NULL,
  phone             varchar(50) NOT NULL,
  addressLine1      varchar(50) NOT NULL,
  addressLine2      varchar(50) DEFAULT NULL,
  state             varchar(50) DEFAULT NULL,
  country           varchar(50) NOT NULL,
  postalCode        varchar(15) NOT NULL,
  territory         varchar(10) NOT NULL,
  TIMESTAMP         TIMESTAMP,
  PRIMARY KEY(officeCode)
);
-- execute the query



-- erase the previous query
-- 2. create employees table, copy this query and paste it
CREATE TABLE IF not EXISTS classicmodels.employees (
  employeeNumber  int NOT NULL,
  lastName        varchar(50) NOT NULL,
  firstName       varchar(50) NOT NULL,
  extension       varchar(10) NOT NULL,
  email           varchar(100) NOT NULL,
  officeCode      varchar(10) NOT NULL,
  reportsTo       int DEFAULT NULL,
  jobTitle        varchar(50) NOT NULL,
  TIMESTAMP       TIMESTAMP,
  PRIMARY KEY(employeeNumber),
  FOREIGN KEY(reportsTo) REFERENCES classicmodels.employees(employeeNumber),
  FOREIGN KEY(officeCode) REFERENCES classicmodels.offices(officeCode)
);
-- execute the query



-- erase the previous query
-- 3. create customers table, copy this query and paste it
CREATE TABLE IF not EXISTS classicmodels.customers (
  customerNumber            int NOT NULL,
  customerName              varchar(50) NOT NULL,
  contactLastName           varchar(50) NOT NULL,
  contactFirstName          varchar(50) NOT NULL,
  phone                     varchar(50) NOT NULL,
  addressLine1              varchar(50) NOT NULL,
  addressLine2              varchar(50) DEFAULT NULL,
  city                      varchar(50) NOT NULL,
  state                     varchar(50) DEFAULT NULL,
  postalCode                varchar(15) DEFAULT NULL,
  country                   varchar(50) NOT NULL,
  salesRepEmployeeNumber    int DEFAULT NULL,
  creditLimit               decimal(10,2),
  TIMESTAMP                 TIMESTAMP,
  PRIMARY KEY(customerNumber),
  FOREIGN KEY(salesRepEmployeeNumber) REFERENCES classicmodels.employees(employeeNumber)
);
-- execute the query



-- erase the previous query
-- 4. create orders table, copy this query and paste it
CREATE TABLE IF not EXISTS classicmodels.orders (
  orderNumber       int NOT NULL,
  orderDate         date NOT NULL,
  requiredDate      date NOT NULL,
  shippedDate       date DEFAULT NULL,
  status            varchar(15) NOT NULL,
  comments          text DEFAULT NULL,
  customerNumber    int NOT NULL,
  TIMESTAMP         TIMESTAMP,
  PRIMARY KEY(orderNumber),
  FOREIGN KEY(customerNumber) REFERENCES classicmodels.customers(customerNumber)
);
-- execute the query



-- erase the previous query
-- 5. create productlines table, copy this query and paste it
CREATE TABLE IF not EXISTS classicmodels.productlines (
  productLine       varchar(50) NOT NULL,
  textDescription   varchar(4000) DEFAULT NULL,
  htmlDescription   varchar(max) DEFAULT NULL,
  image             varchar(max) DEFAULT NULL,
  TIMESTAMP         TIMESTAMP,
  PRIMARY KEY(productLine)
);
-- execute the query



-- erase the previous query
-- 6. create products table, copy this query and paste it
CREATE TABLE IF not EXISTS classicmodels.products (
  productCode           varchar(15) NOT NULL,
  productName           varchar(70) NOT NULL,
  productLine           varchar(50) NOT NULL,
  productScale          varchar(10) NOT NULL,
  productVendor         varchar(50) NOT NULL,
  productDescription    varchar(max) NOT NULL,
  quantityInStock       int NOT NULL,
  buyPrice              decimal(10,2) NOT NULL,
  MSRP                  decimal(10,2) NOT NULL,
  TIMESTAMP             TIMESTAMP,
  PRIMARY KEY(productCode),
  FOREIGN KEY(productLine) REFERENCES classicmodels.productlines(productLine)
);
-- execute the query



-- erase the previous query
-- 7. create orderdetails table, copy this query and paste it
CREATE TABLE IF not EXISTS classicmodels.orderdetails (
  orderNumber       int NOT NULL,
  productCode       varchar(15) NOT NULL,
  quantityOrdered   int NOT NULL,
  priceEach         decimal(10,2) NOT NULL,
  orderLineNumber   int NOT NULL,
  TIMESTAMP         TIMESTAMP,
  PRIMARY KEY(orderNumber,productCode),
  FOREIGN KEY(orderNumber) REFERENCES classicmodels.orders(orderNumber),
  FOREIGN KEY(productCode) REFERENCES classicmodels.products(productCode)
);
-- execute the query



-- erase the previous query
-- 8. create payments table, copy this query and paste it
CREATE TABLE IF not EXISTS classicmodels.payments (
  customerNumber    int NOT NULL,
  checkNumber       varchar(50) NOT NULL,
  paymentDate       date NOT NULL,
  amount            decimal(10,2) NOT NULL,
  TIMESTAMP         TIMESTAMP,
  PRIMARY KEY(customerNumber,checkNumber),
  FOREIGN KEY(customerNumber) REFERENCES classicmodels.customers(customerNumber)
);
-- execute the query