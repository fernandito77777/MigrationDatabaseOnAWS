--	Create redshift_lab schema.
CREATE schema classicmodels;

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
  PRIMARY KEY(officeCode)
);

CREATE TABLE IF not EXISTS classicmodels.employees (
  employeeNumber  int NOT NULL,
  lastName        varchar(50) NOT NULL,
  firstName       varchar(50) NOT NULL,
  extension       varchar(10) NOT NULL,
  email           varchar(100) NOT NULL,
  officeCode      varchar(10) NOT NULL,
  reportsTo       int DEFAULT NULL,
  jobTitle        varchar(50) NOT NULL,
  PRIMARY KEY(employeeNumber),
  FOREIGN KEY(reportsTo) REFERENCES classicmodels.employees(employeeNumber),
  FOREIGN KEY(officeCode) REFERENCES classicmodels.offices(officeCode)
);

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
  PRIMARY KEY(customerNumber),
  FOREIGN KEY(salesRepEmployeeNumber) REFERENCES classicmodels.employees(employeeNumber)
);

CREATE TABLE IF not EXISTS classicmodels.orders (
  orderNumber       int NOT NULL,
  orderDate         date NOT NULL,
  requiredDate      date NOT NULL,
  shippedDate       date DEFAULT NULL,
  status            varchar(15) NOT NULL,
  comments          text DEFAULT NULL,
  customerNumber    int NOT NULL,
  PRIMARY KEY(orderNumber),
  FOREIGN KEY(customerNumber) REFERENCES classicmodels.customers(customerNumber)
);

CREATE TABLE IF not EXISTS classicmodels.productlines (
  productLine       varchar(50) NOT NULL,
  textDescription   varchar(4000) DEFAULT NULL,
  htmlDescription   varchar(max) DEFAULT NULL,
  image             varchar(max) DEFAULT NULL,
  PRIMARY KEY(productLine)
);

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
  PRIMARY KEY(productCode),
  FOREIGN KEY(productLine) REFERENCES classicmodels.productlines(productLine)
);

CREATE TABLE IF not EXISTS classicmodels.orderdetails (
  orderNumber       int NOT NULL,
  productCode       varchar(15) NOT NULL,
  quantityOrdered   int NOT NULL,
  priceEach         decimal(10,2) NOT NULL,
  orderLineNumber   int NOT NULL,
  PRIMARY KEY(orderNumber,productCode),
  FOREIGN KEY(orderNumber) REFERENCES classicmodels.orders(orderNumber),
  FOREIGN KEY(productCode) REFERENCES classicmodels.products(productCode)
);

CREATE TABLE IF not EXISTS classicmodels.payments (
  customerNumber    int NOT NULL,
  checkNumber       varchar(50) NOT NULL,
  paymentDate       date NOT NULL,
  amount            decimal(10,2) NOT NULL,
  PRIMARY KEY(customerNumber,checkNumber),
  FOREIGN KEY(customerNumber) REFERENCES classicmodels.customers(customerNumber)
);

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
  PRIMARY KEY(productCode),
  FOREIGN KEY(productLine) REFERENCES classicmodels.productlines(productLine)
);