# Real-Time Healthcare Data Pipeline

## Overview
This project demonstrates an end-to-end real-time healthcare data pipeline using Apache Kafka, Databricks (Apache Spark), and AWS concepts. The pipeline ingests healthcare events, processes data in batch and streaming modes, applies data quality checks, and produces analytics-ready datasets.

## Architecture
Kafka → Databricks (Spark) → Curated Data → BI / Analytics

## Tech Stack
- Python, SQL
- Apache Kafka
- Databricks (Apache Spark)
- AWS (S3, Lambda – conceptual)
- Data Modeling (Star Schema)

## Key Features
- Real-time ingestion using Kafka producers & consumers
- Batch and streaming processing using Spark
- Schema validation and data quality checks
- Airflow-style orchestration concepts
- Analytics-ready curated datasets

## Use Cases
- Readmission rate analysis
- Length of stay analytics
- Healthcare KPI reporting

## How to Run
1. Start Kafka locally or via Docker
2. Run producer to send events
3. Process data using Spark scripts
4. Validate curated outputs

## Author
Praneeth Madala
