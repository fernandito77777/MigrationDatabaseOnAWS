1. Migration Notes

https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.Homogeneous
https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html
https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting.html#CHAP_Troubleshooting.MySQL
To migrate ongoing, need to change binary logging on /etc/mysql/mysql.conf.d/mysqld.cnf (https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.Homogeneous)

Bucket name: fernandito-datalake-demo-bucket

copy data from local to EC2: scp -i EC2MySQLDB.pem mysqlsampledatabase.sql ubuntu@ec2-54-251-202-116.ap-southeast-1.compute.amazonaws.com:~/