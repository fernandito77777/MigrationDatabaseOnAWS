## Setup Your Database Server

1. Go to [AWS Console](https://console.aws.amazon.com/console/home?region=us-east-1#)
2. Type `EC2` and click the EC2 menu
    ![](../../images/Migration/SetupEC2/2.png)
3. Click `Instances` at the left menu
    ![](../../images/Migration/SetupEC2/3.png)
4. Click `Launch instances`
    ![](../../images/Migration/SetupEC2/4.png)
5. Find `Ubuntu Server 16.04 LTS (HVM)` and click `Select`
    ![](../../images/Migration/SetupEC2/5.png)
6. Click `Next: Configure Instance Details`
7. In Instance Details page, in Network, choose your previously created VPC (`DatabaseVPC`)
8. in subnet, choose subnet `Public 1`
9. Click `Next: Add Storage`
    ![](../../images/Migration/SetupEC2/9.png)
10. On Encryption section, click the dropdown and choose default AWS KMS Key. This is to encrypt the SSD Volume that will be attached to your server.
    ![](../../images/Migration/SetupEC2/10.png)
11. Click `Next: Add Tags`
12. Click `Next: Configure Security Group`
13. Change the Security Group name to `EC2MySQLSG`
14. Fill the description as `EC2 MySQL Security Group`
15. Click `Add Rule`
16. at the new row of Type, click `MYSQL/Aurora`
17. at Source, click `My IP`
18. Click `Add Rule`
19. at the new row of Type, click `MYSQL/Aurora`
20. at Source, type `10.0.0.0/16`
21. Click `Review and Launch`
22. Click `Launch`
23. On Key pair menu, choose `Create a new key pair`
24. Fill the Key pair name as `EC2MySQLKey`
25. Click `Download Key Pair`. key pair file will be downloaded through your computer.
26. Click `Launch Instances`
    ![](../../images/Migration/SetupEC2/26.png)
27. Click `View Instances`

It will take few minutes to access your server until your instance state says `Running`
    ![](../../images/Migration/SetupEC2/27.png)

28. At Name Page, click the pencil icon
29. Edit the name and fill it with `EC2MySQL`
30. Click `Save`
    ![](../../images/Migration/SetupEC2/30.png)
31. Click `Elastic IP` at Network and Security Section
    ![](../../images/Migration/SetupEC2/31.png)
32. Click `Allocate Elastic IP address`
33. Click `Allocate`
34. Check the checkbox of your Elastic IP 
35. Click `Actions` and click `Associate Elastic IP address`
    ![](../../images/Migration/SetupEC2/35.png)

Now, we need to wait until the instance is ready. To know if the instance is ready, check the `Status check` if it says `2/2 checks passed`

36. Choose the instance that you have created (`EC2MySQL`)
37. Choose the private IP address
38. Click `Associate`

this will create the public IP to the instance that you have created.

39. Click `Instance` at the left menu
    ![](../../images/Migration/SetupEC2/39.png)
40. Check the checkbox of your instance
41. Click `Actions` and click `Connect`
    ![](../../images/Migration/SetupEC2/41.png)
42. Click `SSH client`. it will display the way for you to connect to your instance
43. open your terminal and go to the directory of your Key Pair file (`EC2MySQLKey`)
44. Type `chmod 400 EC2MySQLKey.pem`. This will change the permission of your key file.
45. Type 'ssh -i "EC2MySQLKey.pem" ubuntu@`Public DNS of your instance`'. you can find the public DNS instance at the instance page or just copy the instruction at Connect page.
46. Type `yes` and you will be connected to your instance.

Once you are connected, the display at your terminal will be displayed as below:
    ![](../../images/Migration/SetupEC2/46.png)

Now, we need to install MySQL at the server

47. Type `sudo apt-get update`. it will update the apt package.
48. Type `sudo apt-get install mysql-server`
49. input your root password. Remember it!
50. confirm your password.

Once it's done, now you will be able to use MySQL

51. Type `mysql -u root -p`
52. Type your password

it will show mysql interface.
    ![](../../images/Migration/SetupEC2/52.png)

53. Type `exit`

you will be back at your instance. Now, we need to download the sample of the data.

54. Download [this file](../../files/Migration/SetupEC2/mysqlsampledatabase.sql) For database sample creation
55. open the new terminal window. don't close your ubuntu server window

we need to copy from your local into ubuntu server.

56. go to your directory file and make sure your sql file and key file in a same folder.
57. go to [EC2 Console](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Home:)
58. click `instances` at the left menu
59. click the checbox at the left side of your instance (`EC2MySQL`)
60. copy the IPv4 public DNS at the below page.
    ![](../../images/Migration/SetupEC2/60.png)
61. in the new terminal, type `scp -i EC2MySQLKey.pem mysqlsampledatabase.sql ubuntu@Your-Public-DNS:~/`

Now go to your ubuntu terminal

62. type `ls`

you will see the file is being copied successfully at your server.
    ![](../../images/Migration/SetupEC2/62.png)

63. Type `mysql -u root -p < mysqlsampledatabase.sql`
64. input your root password.

It will execute the creation of database and data. Now, we need to check if the query has been executed.

65. Type `mysql -u root -p`
66. input your root password.
67. In SQL Interface, type `SHOW DATABASES;`

You will see `classicmodels` database, which is the dummy database we got from executing the previous query.
    ![](../../images/Migration/SetupEC2/67.png)

We need to create an user to remotely access the database. This user will be used to migrate the database. Don't forget to change the password in below command "Identified by". Remember the password.

68. Type `CREATE USER 'testuser'@'%' identified by 'your password here';`
69. Type `GRANT ALL ON classicmodels.* to 'testuser';`
70. Type `GRANT REPLICATION SLAVE,REPLICATION CLIENT ON *.* TO 'testuser'@'%';`

Once you have done, we need to open the MySQL to be accessible outside. First, we need to stop the SQL first, configure it, then turn it on again.

71. Type `exit`
72. Type `sudo service mysql stop`
73. Type `cd /etc/mysql/mysql.conf.d`

We need to edit the bind address to allow other processes access to the MySQL

74. Type `sudo vim mysqld.cnf`

it will display the configuration file of your MySQL.

75. Type `i` at your keyboard.
76. Find `bind-address` and change it from `127.0.0.1` to `0.0.0.0`

Another thing, we need to turn on the binary log and server id. This binary log will be used to migrate the data we have.

77. find `#server-id = 1` and remove the `#`
78. find `#log_bin = ...` and remove the `#`
79. find `# binlog_do_db = ...` and remove the `#`
80. replace the db name into `classicmodels`
    ![](../../images/Migration/SetupEC2/80.png)
81. Type escape (esc) at your keyboard
82. Type `:wq!`

it will save and quit the text editor. We need to run the MySQL again.

83. Type `sudo service mysql start`

Now, we need to check if the binary logs has been enabled though testuser account.

84. Type `mysql -u testuser -p`
85. Input your testuser password in step 68.
86. In MySQL Interface, type `SHOW BINARY LOGS;`

It will display the binary logs table at the query result.
    ![](../../images/Migration/SetupEC2/86.png)

Now, We need to try the connection.

87. Type `exit`
88. Type `exit` again.

it will come back to your terminal and the connection of your instance is being closed.

We need to try to access the MySQL remotely.

89. go to your [EC2 console here](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#)
90. find your instance (EC2MySQL) and copy the Public IPv4 DNS
    ![](../../images/Migration/SetupEC2/90.png)
91. in your regular terminal, type 'mysql -h `your public IPv4 DNS` -P 3306 -u testuser -p'
92. Type your password

it will be connected to your MySQL at the server. Now, let's see the database.

93. In MySQL interface, type `SHOW DATABASES;`
    ![](../../images/Migration/SetupEC2/93.png)
94. Type `exit`.

[BACK TO WORKSHOP GUIDE](../../README.md)