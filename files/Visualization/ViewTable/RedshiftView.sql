-- 1. offices view
CREATE VIEW classicmodels.offices_vw AS
SELECT
	officeCode,
  	city,
	phone,
    addressLine1,
    addressLine2,
    state,
    country,
    postalCode,
    territory,
    TIMESTAMP
FROM classicmodels.offices
WHERE TIMESTAMP=(SELECT MAX(TIMESTAMP) FROM classicmodels.offices)
-- execute the query



-- erase the previous query
-- 2. employees view
CREATE VIEW classicmodels.employees_vw AS
SELECT
	employeeNumber,
  	lastName,
    firstName,
    extension,
    email,
    officeCode,
    reportsTo,
    jobTitle,
    TIMESTAMP
FROM classicmodels.employees
WHERE TIMESTAMP=(SELECT MAX(TIMESTAMP) FROM classicmodels.employees)
-- execute the query



-- erase the previous query
-- 3. customers view
CREATE VIEW classicmodels.customers_vw AS
SELECT
	customerNumber,
    customerName,
    contactLastName,
    contactFirstName,
    phone,
    addressLine1,
    addressLine2,
    city,
    state,
    postalCode,
    country,
    salesRepEmployeeNumber,
    creditLimit,
    TIMESTAMP
FROM classicmodels.customers
WHERE TIMESTAMP=(SELECT MAX(TIMESTAMP) FROM classicmodels.customers)
-- execute the query



-- erase the previous query
-- 4. orders view
CREATE VIEW classicmodels.orders_vw AS
SELECT
	orderNumber,
    orderDate,
    requiredDate,
    shippedDate,
    status,
    comments,
    customerNumber,
    TIMESTAMP
FROM classicmodels.orders
WHERE TIMESTAMP=(SELECT MAX(TIMESTAMP) FROM classicmodels.orders)
-- execute the query



-- erase the previous query
-- 5. productlines view
CREATE VIEW classicmodels.productlines_vw AS
SELECT
	productLine,
    textDescription,
    htmlDescription,
    image,
    TIMESTAMP
FROM classicmodels.productlines
WHERE TIMESTAMP=(SELECT MAX(TIMESTAMP) FROM classicmodels.productlines)
-- execute the query



-- erase the previous query
-- 6. products view
CREATE VIEW classicmodels.products_vw AS
SELECT
	productCode,
    productName,
    productLine,
    productScale,
    productVendor,
    productDescription,
    quantityInStock,
    buyPrice,
    MSRP,
    TIMESTAMP
FROM classicmodels.products
WHERE TIMESTAMP=(SELECT MAX(TIMESTAMP) FROM classicmodels.products)
-- execute the query



-- erase the previous query
-- 7. orderdetails view
CREATE VIEW classicmodels.orderdetails_vw AS
SELECT
	orderNumber,
    productCode,
    quantityOrdered,
    priceEach,
    orderLineNumber,
    TIMESTAMP
FROM classicmodels.orderdetails
WHERE TIMESTAMP=(SELECT MAX(TIMESTAMP) FROM classicmodels.orderdetails)
-- execute the query



-- erase the previous query
-- 8. payments view
CREATE VIEW classicmodels.payments_vw AS
SELECT
	customerNumber,
    checkNumber,
    paymentDate,
    amount,
    TIMESTAMP
FROM classicmodels.payments
WHERE TIMESTAMP=(SELECT MAX(TIMESTAMP) FROM classicmodels.payments)