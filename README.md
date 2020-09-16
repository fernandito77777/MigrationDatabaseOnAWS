# Migration Database On AWS and Visualize data through QuickSight

### Architecture Diagram
#### Migration
    ![](./images/MigrationArchitecture.png)
#### Data Warehouse
    ![](./images/DWHArchitecture.png)

### Agenda
* Migrate MySQL Database on EC2 Database to AWS RDS (Relational Database Service)
    * 1 - [Setup Your EC2 Database](docs/Migration/SetupEC2.md)
    * 2 - [Setup Networking on AWS](docs/Migration/SetupNetworking.md)
    * 3 - [Create RDS Database](docs/Migration/CreateRDS.md)
    * 4 - [Migrate the Database](docs/Migration/MigrateDB.md)
* Visualize RDS data through QuickSight
    * 1 - [Create and Integrate RDS to Data Lake (S3)](docs/Visualization/IntegrateRDStoDataLake.md)
    * 2 - [ETL (Extract, Transform, Load) from Data Lake to Data Warehouse](docs/Visualization/ETL.md)
    * 3 - [Create Data Warehouse (Redshift)](docs/Visualization/DWH.md)
    * 4 - [Visual Data from Data Warehouse using BI Tools (QuickSight)](docs/Visualization/Visualize.md)

### Scope of Project
* Database will be using MySQL Community version (8.0.20)
* Migration will be done from EC2 MySQL to RDS MySQL
