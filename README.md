# Airops360

Enterprise-Grade Airline Operations Data Pipeline

Airops360 is a modular, cloud-native data pipeline that simulates real-time airline operations and delay prediction. Inspired by real industry experience at Southwest Airlines and Infosys, this project reflects modern data engineering best practices across ingestion, transformation, orchestration, warehousing, and business intelligence.

## Project Overview

- Real-time ingestion of flight delay and weather data using simulated streams
- Batch and streaming ETL with Apache Spark (PySpark)
- Orchestrated pipelines using Apache Airflow
- Data warehouse integration with Snowflake and AWS Redshift
- Executive-level dashboards built in Tableau and Power BI
- Predictive modeling of flight delay likelihood using airline and weather features

## Architecture

Simulated Stream → AWS S3 → PySpark Transformations → Snowflake/Redshift → Tableau Dashboard

## Tech Stack

Component | Tools Used  
--- | ---  
Ingestion | Simulated Kafka, AWS Lambda  
Storage | AWS S3, Azure Blob  
Processing | PySpark, AWS Glue, Databricks  
Orchestration | Apache Airflow  
Data Warehouse | Snowflake, AWS Redshift  
BI & Visualization | Tableau, Power BI  
ML (Optional) | Sklearn, Spark MLlib  

## Dashboard Preview

Dashboards include:
- Flight delay rate by airport
- Delay forecast for upcoming 7 days
- Cost of delays by airline
- Route-level efficiency analysis

A public Tableau link will be added upon dashboard completion.

## Project Structure

Airops360/  
├── airflow/          - Airflow DAGs  
├── spark_jobs/       - PySpark scripts  
├── data/             - Raw and clean sample datasets  
├── warehouse/        - Snowflake/Redshift schema and queries  
├── ml/               - Delay prediction model (optional)  
├── dashboards/       - Tableau or Power BI screenshots  
├── images/           - Architecture diagram and visuals  
└── README.md         - Project overview  

## Author

Sireesha Prattipati  
This project was designed to reflect practical airline data engineering scenarios similar to those I supported in previous roles. It highlights my experience with enterprise pipelines, multi-cloud architecture, and real-time analytics delivery.
