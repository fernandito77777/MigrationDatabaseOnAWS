import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, unix_timestamp, to_date
from pyspark.sql.functions import current_timestamp

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

customers = glueContext.create_dynamic_frame.from_catalog(database = "classicmodels", table_name = "classicmodels_classicmodels_customers")
employees = glueContext.create_dynamic_frame.from_catalog(database = "classicmodels", table_name = "classicmodels_classicmodels_employees")
offices = glueContext.create_dynamic_frame.from_catalog(database = "classicmodels", table_name = "classicmodels_classicmodels_offices")
orderdetails = glueContext.create_dynamic_frame.from_catalog(database = "classicmodels", table_name = "classicmodels_classicmodels_orderdetails")
orders = glueContext.create_dynamic_frame.from_catalog(database = "classicmodels", table_name = "classicmodels_classicmodels_orders")
payments = glueContext.create_dynamic_frame.from_catalog(database = "classicmodels", table_name = "classicmodels_classicmodels_payments")
productlines = glueContext.create_dynamic_frame.from_catalog(database = "classicmodels", table_name = "classicmodels_classicmodels_productlines")
products = glueContext.create_dynamic_frame.from_catalog(database = "classicmodels", table_name = "classicmodels_classicmodels_products")



#customers table
connection_options_customers = {
    "dbtable": "classicmodels.customers",
    "database": "dev"
}

# Please replace your name here
output_dir_tmp = "s3://fernandito-datalake-demo-bucket/LakeFormation"

#Add timestamp
customers = customers.toDF().withColumn("Timestamp",current_timestamp())
customers = DynamicFrame.fromDF(customers, glueContext, "customers_dynamicframe")

#Mapping data from data catalog to Redshift table
customers = ApplyMapping.apply(frame = customers, 
                                mappings = [
                                    ("customerNumber", "int", "customerNumber", "int"), 
                                    ("customerName", "string", "customerName", "string"), 
                                    ("contactLastName", "string", "contactLastName", "string"),
                                    ("contactFirstName", "string", "contactFirstName", "string"), 
                                    ("phone", "string", "phone", "string"), 
                                    ("addressLine1", "string", "addressLine1", "string"), 
                                    ("addressLine2", "string", "addressLine2", "string"), 
                                    ("city", "string", "city", "string"), 
                                    ("state", "string", "state", "string"), 
                                    ("postalCode", "string", "postalCode", "string"), 
                                    ("country", "string", "country", "string"), 
                                    ("salesRepEmployeeNumber", "int", "salesRepEmployeeNumber", "int"), 
                                    ("creditLimit", "decimal", "creditLimit", "decimal"),
                                    ("Timestamp","timestamp","Timestamp","timestamp")
                                ])

#Load to Redshift
try:
    print("INFO: Loading customer data into Amazon Redshift")
    glueContext.write_dynamic_frame.from_jdbc_conf(frame = customers,
                                                   catalog_connection = "RedshiftConnection",
                                                   connection_options = connection_options_customers,
                                                   redshift_tmp_dir = output_dir_tmp + "/tmp/")
    print("INFO: customer data loading into Amazon Redshift complete")
except Exception as e:
    print("ERROR: An exception has occured: " + str(e))




#employees table
connection_options_employees = {
    "dbtable": "classicmodels.employees",
    "database": "dev"
}

#Add timestamp
employees = employees.toDF().withColumn("Timestamp",current_timestamp())
employees = DynamicFrame.fromDF(employees, glueContext, "employees_dynamicframe")

#Mapping data from data catalog to Redshift table
employees = ApplyMapping.apply(frame = employees, 
                                    mappings = [
                                        ("employeeNumber", "int", "employeeNumber", "int"), 
                                        ("lastName", "string", "lastName", "string"), 
                                        ("firstName", "string", "firstName", "string"),
                                        ("extension", "string", "extension", "string"), 
                                        ("email", "string", "email", "string"), 
                                        ("officeCode", "string", "officeCode", "string"), 
                                        ("reportsTo", "int", "reportsTo", "int"), 
                                        ("jobTitle", "string", "jobTitle", "string"),
                                        ("Timestamp","timestamp","Timestamp","timestamp")
                                    ])

#Load to Redshift
try:
    print("INFO: Loading Employees data into Amazon Redshift")
    glueContext.write_dynamic_frame.from_jdbc_conf(frame = employees,
                                                   catalog_connection = "RedshiftConnection",
                                                   connection_options = connection_options_employees,
                                                   redshift_tmp_dir = output_dir_tmp + "/tmp/")
    print("INFO: Employees data loading into Amazon Redshift complete")
except Exception as e:
    print("ERROR: An exception has occured: " + str(e))



#offices table
connection_options_offices = {
    "dbtable": "classicmodels.offices",
    "database": "dev"
}

#Add timestamp
offices = offices.toDF().withColumn("Timestamp",current_timestamp())
offices = DynamicFrame.fromDF(offices, glueContext, "offices_dynamicframe")

#Mapping data from data catalog to Redshift table
offices = ApplyMapping.apply(frame = offices, 
                                mappings = [
                                    ("officeCode", "string", "officeCode", "string"), 
                                    ("city", "string", "city", "string"), 
                                    ("phone", "string", "phone", "string"),
                                    ("addressLine1", "string", "addressLine1", "string"), 
                                    ("addressLine2", "string", "addressLine2", "string"), 
                                    ("state", "string", "state", "string"), 
                                    ("country", "string", "country", "string"), 
                                    ("postalCode", "string", "postalCode", "string"),
                                    ("territory", "string", "territory", "string"),
                                    ("Timestamp","timestamp","Timestamp","timestamp")
                                ])

#Load to Redshift
try:
    print("INFO: Loading offices data into Amazon Redshift")
    glueContext.write_dynamic_frame.from_jdbc_conf(frame = offices,
                                                   catalog_connection = "RedshiftConnection",
                                                   connection_options = connection_options_offices,
                                                   redshift_tmp_dir = output_dir_tmp + "/tmp/")
    print("INFO: offices data loading into Amazon Redshift complete")
except Exception as e:
    print("ERROR: An exception has occured: " + str(e))



#orderdetails table
connection_options_orderdetails = {
    "dbtable": "classicmodels.orderdetails",
    "database": "dev"
}

# Convert short fields into integer and Add Timestamp
orderdetails = orderdetails.toDF().selectExpr("cast(orderNumber as int) orderNumber",
                                             "cast(productCode as string) productCode",
                                             "cast(quantityOrdered as int) quantityOrdered",
                                             "cast(priceEach as decimal) priceEach",
                                             "cast(orderLineNumber as int) orderLineNumber")
orderdetails = orderdetails.withColumn("Timestamp",current_timestamp())
orderdetails = DynamicFrame.fromDF(orderdetails, glueContext, "orderdetails_dynamicframe")

#Mapping data from data catalog to Redshift table
orderdetails = ApplyMapping.apply(frame = orderdetails, 
                                    mappings = [
                                        ("orderNumber", "int", "orderNumber", "int"), 
                                        ("productCode", "string", "productCode", "string"), 
                                        ("quantityOrdered", "int", "quantityOrdered", "int"),
                                        ("priceEach", "decimal", "priceEach", "decimal"), 
                                        ("orderLineNumber", "int", "orderLineNumber", "int"),
                                        ("Timestamp","timestamp","Timestamp","timestamp")
                                    ])

#Load to Redshift
try:
    print("INFO: Loading orderdetails data into Amazon Redshift")
    glueContext.write_dynamic_frame.from_jdbc_conf(frame = orderdetails,
                                                   catalog_connection = "RedshiftConnection",
                                                   connection_options = connection_options_orderdetails,
                                                   redshift_tmp_dir = output_dir_tmp + "/tmp/")
    print("INFO: orderdetails data loading into Amazon Redshift complete")
except Exception as e:
    print("ERROR: An exception has occured: " + str(e))



#orders table
connection_options_orders = {
    "dbtable": "classicmodels.orders",
    "database": "dev"
}

# convert string to date and add timestamp
orders = orders.toDF().withColumn('orderDateNew', 
                   to_date(unix_timestamp(col('orderDate'), 'yyyy-MM-dd').cast("timestamp"))).withColumn('requiredDateNew', 
                   to_date(unix_timestamp(col('requiredDate'), 'yyyy-MM-dd').cast("timestamp"))).withColumn('shippedDateNew', 
                   to_date(unix_timestamp(col('shippedDate'), 'yyyy-MM-dd').cast("timestamp")))
orders = orders.drop('orderDate').drop('requiredDate').drop('shippedDate')
orders = orders.withColumn("Timestamp",current_timestamp())
orders = DynamicFrame.fromDF(orders, glueContext, "orders_dynamicframe")

#Mapping data from data catalog to Redshift table
orders = ApplyMapping.apply(frame = orders, 
                                mappings = [
                                    ("orderNumber", "int", "orderNumber", "int"),
                                    ("status", "string", "status", "string"), 
                                    ("comments", "string", "comments", "string"), 
                                    ("customerNumber", "int", "customerNumber", "int"),
                                    ("orderDateNew", "date", "orderDate", "date"), 
                                    ("requiredDateNew", "date", "requiredDate", "date"),
                                    ("shippedDateNew", "date", "shippedDate", "date"),
                                    ("Timestamp","timestamp","Timestamp","timestamp")
                                ])

#Load to Redshift
try:
    print("INFO: Loading orders data into Amazon Redshift")
    glueContext.write_dynamic_frame.from_jdbc_conf(frame = orders,
                                                   catalog_connection = "RedshiftConnection",
                                                   connection_options = connection_options_orders,
                                                   redshift_tmp_dir = output_dir_tmp + "/tmp/")
    print("INFO: orders data loading into Amazon Redshift complete")
except Exception as e:
    print("ERROR: An exception has occured: " + str(e))



#Payments table
connection_options_payments = {
    "dbtable": "classicmodels.payments",
    "database": "dev"
}

# add timestamp
payments = payments.toDF().withColumn("Timestamp",current_timestamp())
payments = DynamicFrame.fromDF(payments, glueContext, "payments_dynamicframe")

#Mapping data from data catalog to Redshift table
payments = ApplyMapping.apply(frame = payments, 
                                mappings = [
                                    ("customerNumber", "int", "customerNumber", "int"), 
                                    ("checkNumber", "string", "checkNumber", "string"), 
                                    ("amount", "decimal", "amount", "decimal"),
                                    ("paymentDate", "date", "paymentDate", "date"),
                                    ("Timestamp","timestamp","Timestamp","timestamp")
                                ])

#Load to Redshift
try:
    print("INFO: Loading payments data into Amazon Redshift")
    glueContext.write_dynamic_frame.from_jdbc_conf(frame = payments,
                                                   catalog_connection = "RedshiftConnection",
                                                   connection_options = connection_options_payments,
                                                   redshift_tmp_dir = output_dir_tmp + "/tmp/")
    print("INFO: payments data loading into Amazon Redshift complete")
except Exception as e:
    print("ERROR: An exception has occured: " + str(e))



#productlines table
connection_options_productlines = {
    "dbtable": "classicmodels.productlines",
    "database": "dev"
}

# Convert binary to string and add timestamp
productlines = productlines.toDF()
productlines = productlines.withColumn("imageNew", productlines["image"].cast("string"))
productlines = productlines.drop('image')
productlines = productlines.withColumn("Timestamp",current_timestamp())
productlines = DynamicFrame.fromDF(productlines, glueContext, "productlines_dynamicframe")

#Mapping data from data catalog to Redshift table
productlines = ApplyMapping.apply(frame = productlines, 
                                    mappings = [
                                        ("productLine", "string", "productLine", "string"), 
                                        ("textDescription", "string", "textDescription", "string"), 
                                        ("htmlDescription", "string", "htmlDescription", "string"),
                                        ("imageNew", "string", "image", "string"),
                                        ("Timestamp","timestamp","Timestamp","timestamp")
                                    ])

#Load to Redshift
try:
    print("INFO: Loading productlines data into Amazon Redshift")
    glueContext.write_dynamic_frame.from_jdbc_conf(frame = productlines,
                                                   catalog_connection = "RedshiftConnection",
                                                   connection_options = connection_options_productlines,
                                                   redshift_tmp_dir = output_dir_tmp + "/tmp/")
    print("INFO: productlines data loading into Amazon Redshift complete")
except Exception as e:
    print("ERROR: An exception has occured: " + str(e))



#products table
connection_options_products = {
    "dbtable": "classicmodels.products",
    "database": "dev"
}

# Convert binary to string, short integer to integer, and add timestamp
products = products.toDF()
products = products.withColumn("productScaleNew", products["productScale"].cast("string"))
products = products.drop('productScale')
products = products.selectExpr("cast(productCode as string) productCode",
                              "cast(productName as string) productName",
                              "cast(productLine as string) productLine",
                              "cast(productVendor as string) productVendor",
                              "cast(productDescription as string) productDescription",
                              "cast(quantityInStock as int) quantityInStock",
                              "cast(buyPrice as decimal) buyPrice",
                              "cast(MSRP as decimal) MSRP",
                              "cast(productScaleNew as string) productScaleNew")
products = products.withColumn("Timestamp",current_timestamp())
products = DynamicFrame.fromDF(products, glueContext, "products_dynamicframe")

#Mapping data from data catalog to Redshift table
products = ApplyMapping.apply(frame = products, 
                                mappings = [
                                    ("productCode", "string", "productCode", "string"), 
                                    ("productName", "string", "productName", "string"), 
                                    ("productLine", "string", "productLine", "string"),
                                    ("productVendor", "string", "productVendor", "string"),
                                    ("productDescription", "string", "productDescription", "string"),
                                    ("quantityInStock", "int", "quantityInStock", "int"),
                                    ("buyPrice", "decimal", "buyPrice", "decimal"),
                                    ("MSRP", "decimal", "MSRP", "decimal"),
                                    ("productScaleNew", "string", "productScale", "string"),
                                    ("Timestamp","timestamp","Timestamp","timestamp")
                                ])

#Load to Redshift
try:
    print("INFO: Loading products data into Amazon Redshift")
    glueContext.write_dynamic_frame.from_jdbc_conf(frame = products,
                                                   catalog_connection = "RedshiftConnection",
                                                   connection_options = connection_options_products,
                                                   redshift_tmp_dir = output_dir_tmp + "/tmp/")
    print("INFO: products data loading into Amazon Redshift complete")
except Exception as e:
    print("ERROR: An exception has occured: " + str(e))