# Migration Database On AWS and Visualize data through QuickSight

### Architecture Diagram
#### Migration
    ![](images/Readme/MigrationArchitecture.png)
#### Data Warehouse
    ![](images/Readme/DWHArchitecture.png)

### Agenda
* Migrate MySQL Database on EC2 Database to AWS RDS (Relational Database Service)
    * 1 - [Setup Networking on AWS](docs/Migration/SetupNetworking.md)
    * 2 - [Setup Your Database Server](docs/Migration/SetupEC2.md)
    * 3 - [Create RDS Database](docs/Migration/CreateRDS.md)
    * 4 - [Migrate the Database](docs/Migration/MigrateDB.md)
* Visualize RDS data through QuickSight
    * 1 - [Create and Integrate RDS to Data Lake (S3)](docs/Visualization/IntegrateRDStoDataLake.md)
    * 2 - [Create Data Warehouse (Redshift)](docs/Visualization/DWH.md)
    * 3 - [ETL (Extract, Transform, Load) from Data Lake to Data Warehouse](docs/Visualization/ETL.md)
    * 4 - [Visual Data from Data Warehouse using BI Tools (QuickSight)](docs/Visualization/Visualize.md)

### Scope of Project
* Migration will be done from EC2 MySQL to RDS MySQL
* All services will be on region us-east-1 (North Virginia)
* The instruction is for Mac User. Please use PuTTY to connect to terminal if you are using Windows.