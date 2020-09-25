## Visual Data from Data Warehouse using BI Tools (QuickSight)

1. Go to [AWS Console](https://console.aws.amazon.com/console/home?region=us-east-1#)
2. go to quicksight and register.
3. in permission, choose S3 bucket that you have created.
4. In redshift VPC default, attach Internet gateway
5. enable redshift cluster to be public.
6. go to [this link](https://docs.aws.amazon.com/quicksight/latest/user/regions.html)
7. find north virginia IP address range
8. change the Security group of Redshift cluster and add TCP with port as same as redshift cluster port and add the ip address.
9. try to connect to quicksight.

[BACK TO WORKSHOP GUIDE](../../README.md)