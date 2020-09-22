## Migrate the Database

1. Go to [AWS Console](https://console.aws.amazon.com/console/home?region=us-east-1#)
2. Type `DMS` and click the Database Migration Service menu
    ![](../../images/Migration/MigrateDB/2.png)
3. Click Replication instances at the left menu
4. Click "Create replication instance"
    ![](../../images/Migration/MigrateDB/4.png)
5. Fill the name as "EC2toRDSRepInstance"
6. Fill the description as "Replication Instance from EC2 MySQL to RDS MySQL"
    ![](../../images/Migration/MigrateDB/6.png)
7. in VPC Section, choose the VPC you have created ("DatabaseVPC")
8. Click "Create" at the bottom page.

It might take few minutes to be ready. wait until the status is "Available"
    ![](../../images/Migration/MigrateDB/8.png)

9. Click "Endpoints" at the left menu
10. Click "Create endpoint"
    ![](../../images/Migration/MigrateDB/10.png)
11. Click "Source endpoint"
12. In Endpoint identifier, type "EC2Endpoint"
13. In source engine, choose "mysql"
    ![](../../images/Migration/MigrateDB/13.png)

We need to get the Public IPv4 DNS of the EC2, which is your database server. Don't close DMS window, we will get back there later.

14. Go to [EC2 Console](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#) at the other window/tab
15. Click "Instances" at the left menu
16. Click the checkbox of your EC2 instance ("EC2MySQL")
17. Now, copy the Public IPv4 DNS at the details of your instance.
    ![](../../images/Migration/MigrateDB/17.png)

Now, we need to go back to DMS window.

18. Paste your IPv4 DNS at the server name
19. Fill the port into "3306"
20. Fill the username as "testuser"
21. Fill your password that you have set during making database at your server.
    ![](../../images/Migration/MigrateDB/21.png)
22. Open "Test endpoint connection" section. We are going to test it before creating it.
23. Choose VPC that you have created ("DatabaseVPC")
24. Click "Run test"

wait for a while since it will try to connect.

25. The status will change into "successful"
26. Click "Create endpoint"
    ![](../../images/Migration/MigrateDB/26.png)

We have created the endpoint from the database server. now, we need to create another endpoint for RDS database.

27. Click "Create endpoint"
28. Click "Target endpoint"
29. Click the checkbox of "Select RDS DB instance"
30. Choose your RDS instance ("rdsmysql")
    ![](../../images/Migration/MigrateDB/30.png)
31. Replace the endpoint identifier as "RDSEndpoint"
32. Fill the password of your RDS Database. You have inputted it during RDS Database creation.
33. Go to Test endpoint connection, and select your VPC ("DatabaseVPC")
34. Click "Run test"

Same as previous, we need to wait for a while.

35. the status will change into "successful"
36. Click "Create endpoint"
    ![](../../images/Migration/MigrateDB/36.png)

We have created both endpoints. Now it's time to do the migration.

37. Click "Database migration tasks" at the left menu
38. Click "Create task"
    ![](../../images/Migration/MigrateDB/38.png)
39. Fill the task identifier as "EC2toRDSTask"
40. Choose the replication instance you have created ("EC2toRDSRepInstance)
41. Choose the source database endpoint ("EC2Endpoint")
42. Choose the target database endpoint ("RDSEndpoint")
43. Choose the migration type as "Migrate existing data"
    ![](../../images/Migration/MigrateDB/43.png)
44. Click "Enable CloudWatch logs" at Task settings
    ![](../../images/Migration/MigrateDB/44.png)
45. In table mappings, click "Add new selection rule"
46. In Schema, choose "Enter a schema"
47. on Schema name, replace the schema name to "classicmodels"
    ![](../../images/Migration/MigrateDB/47.png)
48. Click "Create task" at the bottom of the page.
    ![](../../images/Migration/MigrateDB/48.png)

Now, it will automatically migrate the database from EC2 (Database server) to RDS Instance. it will take several minutes to migrate the data.

Once it's done, it will display the status of "Running", and then it will change to "Load Complete"


We need to check the database if it's now available on RDS.
49. Open your terminal
50. Type 'mysql -h `your RDS Endpoint` -P 3306 -u admin -p'
51. Type your RDS Password
52. at MySQL interface, type "SHOW DATABASES;"

it will display classicmodels database from EC2 (your database server)
    ![](../../images/Migration/MigrateDB/52.png)
    
[BACK TO WORKSHOP GUIDE](../../README.md)