# Stock Market Lakehouse - Azure Data Engineering Project

## Introduction

This project implements a complete end-to-end data engineering pipeline using Azure Event Hub, Azure SQL Database, Azure Databricks, and Power BI, following the Medallion Architecture. The use case focuses on collecting and analyzing financial stock market data through an external API, processed in batch using Event Hub triggers.

---

## Project Overview

We simulate a near real-time financial application that collects stock prices periodically from a public API. Data is ingested in batches and processed through different stages (Bronze, Silver, and Gold), ultimately serving insights in Power BI.

## Key Features

- Batch ingestion from a stock market API (e.g., TwelveData, Alpha Vantage)
- Event Hub trigger to manage batch pulling
- Azure SQL Database to temporarily store data
- Databricks Bronze Layer: Raw data ingestion
- Databricks Silver Layer: Data cleansing, formatting, deduplication
- Databricks Gold Layer: Aggregated metrics, business KPIs
- Power BI for visualization
- Data Lake Gen2 containers per medallion layer

---

## Architecture Diagram

<div align="center">
    <img src="https://raw.githubusercontent.com/juancarlosierrac/Stock_Market_Lakehouse-Azure_Data_Engineering_Project/main/images/Stock Market Lakehouse.png" 
         alt="Stock Market Lakehouse.png" 
         width="1000px"/>
</div>

---

## Objective

To build a financial stock data pipeline using modern data engineering practices with Azure tools:

- Simulate a stock price ingestion system
- Demonstrate Lakehouse concepts in practice
- Showcase real-time analytics and visualization

---

## Technologies Used

- Azure Event Hub  
- Azure SQL Database  
- Azure Databricks  
- Azure Data Lake Storage Gen2  
- Delta Lake  
- Azure Key Vault  
- Power BI  
- GitHub  
- Python (requests, pyodbc, pandas)
---

## 