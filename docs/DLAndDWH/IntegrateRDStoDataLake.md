## Create and Integrate RDS to Data Lake (S3)

1. Go to [AWS Console](https://console.aws.amazon.com/console/home?region=us-east-1#)
2. Type `RDS` and click the RDS menu
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/2.png)
3. Click `Snapshots` at the left menu
4. click `Take snapshot`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/4.png)
5. Choose the RDS DB instance you have created (`rdsmysql`)
6. fill the snapshot name as `RDSSnapshot`
7. Click `Take snapshot`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/7.png)

It will take several minutes to create the snapshot. during that, we need to create Encryption key as a required step to export the snapshot from RDS to S3, which is going to be our data lake.

8. Go to [KMS Console](https://console.aws.amazon.com/kms/home?region=us-east-1#/kms/keys)
9. Click `Create key`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/9.png)
10. Choose `Symmetric` key
11. click `Next`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/11.png)
12. In Alias, type `RDSSnapshotKey`
13. click `Next`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/13.png)
14. in define key administrative permission, click `Next`
15. in define key usage permissions, click `Next`
16. in Review and edit key policy, click `Finish`

after creating key, we need to create the bucket.

17. go to [S3 Console](https://s3.console.aws.amazon.com/s3/home?region=us-east-1#)
18. click `Create bucket`
19. in bucket name, type `yourname-demo-datalake-bucket`
20. click `Next`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/20.png)
21. in properties page, click `Next`
22. in block all public access, make sure the checkbox is being checked
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/22.png)
23. click `Next`
24. click `Create bucket`

now, we can back to RDS Console to check if the snapshot has been created

25. go to [RDS Console Snapshot Menu](https://console.aws.amazon.com/rds/home?region=us-east-1#snapshots-list:)
26. click the name of your snapshot (`rdssnapshot`)
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/26.png)
27. click `Actions` then click `Export to Amazon S3`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/27.png)

it will display the export page

28. In export identifier, type `rdsexporttos3`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/28.png)
29. In S3 destination, choose your bucket (`yourname-demo-datalake-bucket`)
30. In S3 Prefix, type `RDSSnapshot/`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/30.png)
31. in IAM role, choose `Create a new role`
32. fill the IAM role name as `RDSExportToS3Role`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/32.png)
33. in Encryption, choose the key you have created (`RDSSnapshotKey)
34. Click `Export to Amazon S3`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/34.png)

during creation, you may encounter the error says that the role isn't authorized to call S3 put object
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/34-2.png)

We need to attach this to the role you have created.

35. go to [IAM Console](https://console.aws.amazon.com/iam/home?region=us-east-1)
36. click `Roles` at the left menu
37. in search bar, type `RDSExportToS3Role`. click the role name
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/37.png)
38. in permission tab, click `Attach policies`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/38.png)
39. in search bar, type `S3FullAccess`. It will show one policy
40. click the checbox besides `AmazonS3FullAccess`
41. click `Attach policy`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/41.png)

Once we have give the permission to access our data lake, we need to go back to the RDS Page.

42. go to [RDS Console Snapshot Menu](https://console.aws.amazon.com/rds/home?region=us-east-1#snapshots-list:)
43. click the name of your snapshot (`rdssnapshot`)
44. click `Actions` then click `Export to Amazon S3`

Like the previous step number 28 until 34, we need to do it again. but, we need to change a little bit about the authorization part.

45. In export identifier, type `rdsexporttos3`
46. In S3 destination, choose your bucket (`yourname-demo-datalake-bucket`)
47. In S3 Prefix, type `RDSSnapshot/`
48. in IAM role, search `RDSExportToS3Role` and click the role.
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/48.png)
49. in Encryption, choose the key you have created (`RDSSnapshotKey`)
50. Click `Export to Amazon S3`

it will start to export the snapshot from your RDS Database to Data lake (S3)

This process will take several minutes. 

once it's done, it will show the status as `Complete`
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/50.png)

We need to check the data if it's avaliable at the data lake now.

51. go to [S3 Console](https://s3.console.aws.amazon.com/s3/home?region=us-east-1#)
52. Click your bucket name
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/52.png)
53. it will display the RDSSnapshot Folder inside. Click the folder
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/53.png)
54. You will see another folder inside. click that folder
55. it will display your database folder name (`classicmodels`)
    ![](../../images/DLAndDWH/IntegrateRDStoDataLake/55.png)

It means, your data has been exported to your data lake (S3)

[BACK TO WORKSHOP GUIDE](../../README.md)