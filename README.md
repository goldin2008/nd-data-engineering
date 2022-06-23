# Data Engineering Nanodegree Program

#### Project 1: Data Modeling with Postgres
Students will model user activity data to create a database and ETL pipeline in Postgres for a music streaming app. They will define Fact and Dimension tables and insert data into new tables.

#### Project 2: Data Modeling with Apache Cassandra
Students will model event data to create a non-relational database and ETL pipeline for a music streaming app. They will define queries and tables for a database built using Apache Cassandra.

#### Project 3: Data Warehouse
Students will build an ETL pipeline that extracts data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team.

#### Project 4: Data Lake
Students will build a data lake and an ETL pipeline in Spark that loads data from S3, processes the data into analytics tables, and loads them back into S3.

#### Project 5: Data Pipelines
Students continue to work on the music streaming company’s data infrastructure by creating and automating a set of data pipelines with Airflow, monitoring and debugging production pipelines

#### Capstone Project
In this Capstone project, students will define the scope of the project and the data they will be working with to demonstrate what they have learned in this Data Engineering Nanodegree.


Projects and resources developed in the [DEND Nanodegree](https://www.udacity.com/course/data-engineer-nanodegree--nd027) from Udacity.

> https://github.com/vanducng/Data-Engineering-HowTo

> https://github.com/danieldiamond/udacity-dend

### Project 1: Data Modeling with Postgres
<p align="center"><img src="https://raw.githubusercontent.com/danieldiamond/udacity-dend/master/relational_db_modeling_postgresql/images/logo.png" style="height: 100%; width: 100%; max-width: 200px" /></p>

Developed a relational database using PostgreSQL to model user activity data for a music streaming app. Skills include:
* Created a relational database using PostgreSQL
* Developed a Star Schema database using optimized definitions of Fact and Dimension tables. Normalization of tables.
* Built out an ETL pipeline to optimize queries in order to understand what songs users listen to.

Proficiencies include: Python, PostgreSql, Star Schema, ETL pipelines, Normalization

Students will model user activity data to create a database and ETL pipeline in Postgres for a music streaming app. They will define Fact and Dimension tables and insert data into new tables.

https://github.com/BaiHuang89/DataModelingWithPostgres

### Project 2: Data Modeling with Apache Cassandra
<p align="center"><img src="https://raw.githubusercontent.com/danieldiamond/udacity-dend/master/nosql_db_modeling_apache_cassandra/images/logo.png" style="height: 100%; width: 100%; max-width: 200px" /></p>

Designed a NoSQL database using Apache Cassandra based on the original schema outlined in project one. Skills include:
* Created a nosql database using Apache Cassandra (both locally and with docker containers)
* Developed denormalized tables optimized for a specific set queries and business needs

Proficiencies used: Python, Apache Cassandra, Denormalization

Students will model event data to create a non-relational database and ETL pipeline for a music streaming app. They will define queries and tables for a database built using Apache Cassandra.

### Project 3: Data Warehouse
<p align="center"><img src="https://raw.githubusercontent.com/danieldiamond/udacity-dend/master/data_warehouse_redshift/images/logo.png" style="height: 100%; width: 100%; max-width: 200px" /></p>

Created a database warehouse utilizing Amazon Redshift. Skills include:
* Creating a Redshift Cluster, IAM Roles, Security groups.
* Develop an ETL Pipeline that copies data from S3 buckets into staging tables to be processed into a star schema
* Developed a star schema with optimization to specific queries required by the data analytics team.

Proficiencies used: Python, Amazon Redshift, aws cli, Amazon SDK, SQL, PostgreSQL

Students will build an ETL pipeline that extracts data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team.

https://github.com/rakeshpaulraj/Datawarehouse_on_AWS_Redshift

https://github.com/jkoth/DW-on-AWS-Redshift

### Project 4: Data Lake
<p align="center"><img src="https://raw.githubusercontent.com/danieldiamond/udacity-dend/master/data_lake_spark/images/logo.png" style="height: 100%; width: 100%; max-width: 200px" /></p>

Scaled up the current ETL pipeline by moving the data warehouse to a data lake. Skills include:
* Create an EMR Hadoop Cluster
* Further develop the ETL Pipeline copying datasets from S3 buckets, data processing using Spark and writing to S3 buckets using efficient partitioning and parquet formatting.
* Fast-tracking the data lake buildout using (serverless) AWS Lambda and cataloging tables with AWS Glue Crawler.

Technologies used: Spark, S3, EMR, Athena, Amazon Glue, Parquet.

Students will build a data lake and an ETL pipeline in Spark that loads data from S3, processes the data into analytics tables, and loads them back into S3.

https://github.com/jkoth/Data-Lake-with-Spark-and-AWS-S3

### Project 5: Data Pipelines
<p align="center"><img src="https://raw.githubusercontent.com/danieldiamond/udacity-dend/master/data_pipelines_airflow/images/logo.png" style="height: 100%; width: 100%; max-width: 200px" /></p>

Automate the ETL pipeline and creation of data warehouse using Apache Airflow. Skills include:
* Using Airflow to automate ETL pipelines using Airflow, Python, Amazon Redshift.
* Writing custom operators to perform tasks such as staging data, filling the data warehouse, and validation through data quality checks.
* Transforming data from various sources into a star schema optimized for the analytics team's use cases.

Technologies used: Apache Airflow, S3, Amazon Redshift, Python.

Students continue to work on the music streaming company’s data infrastructure by creating and automating a set of data pipelines with Airflow, monitoring and debugging production pipelines

https://github.com/benjigoldberg/udacity-airflow

https://github.com/brfulu/airflow-data-pipeline

https://github.com/sbwhitney/data-pipelines-airflow

https://github.com/chsanch/udacity-den-data-pipelines

https://github.com/jaycode/udacity-data_pipelines

https://github.com/HazalCiplak/Data-Pipelines-with-Airflow

https://github.com/alvarocuervo/Udacity-PRO5-Data_Pipelines

https://github.com/pavanrao/Sparkify-Data-Pipelines-with-Airflow

https://github.com/rhoneybul/udacity-dend-data-pipelines

https://github.com/Katba-Caroline/Data-Pipelines-with-Airflow

https://github.com/johnjairo25/udacity-data-eng-data-pipelines

https://github.com/Sarwan-S/udacity-nanodegree-data-pipelines

https://github.com/npatta01/udacity-dataengineer-data-pipelines-project

https://github.com/ulmefors/udacity-nd027-data-pipelines

https://github.com/GourBera/Data-Pipelines-with-Apache-Airflow

https://github.com/NileshPPatel/Udacity-DataEngineering-Data-Pipelines-with-Airflow#project-data-pipelines

https://github.com/xingyazhou/udacity-data-pipelines-with-airflow

### Capstone Project
In this Capstone project, students will define the scope of the project and the data they will be working with to demonstrate what they have learned in this Data Engineering Nanodegree.

https://github.com/dysartcoal/DataPipeline_AirflowSparkEMR

https://github.com/xingyazhou/udacity-dend-capstone-project

https://github.com/jukkakansanaho/udacity-dend-project-capstone

https://github.com/brfulu/us-accidents-data-engineering

======

https://github.com/kudeh/udacity-dend-capstone

https://github.com/dai-dao/udacity-data-engineering-capstone

https://github.com/rossgray/udacity-data-eng-project

https://github.com/gruszkam/data-engineering-capstone

https://github.com/sortizm/DataEngineeringUdacity

https://github.com/weinanlee/data-engineering-capstone-project

https://github.com/cyonglun/udacity-data-engineering-capstone
