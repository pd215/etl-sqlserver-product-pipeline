# etl-sqlserver-product-pipeline
End-to-end data engineering pipeline using Python and SQL Server with ETL, star schema modeling and analytics layer.

# Logistics Data Pipeline (End-to-End Data Engineering Project)

##  Overview

This project demonstrates a complete end-to-end data engineering pipeline built using Python and SQL Server.

The pipeline ingests data from an external API, processes it through a structured ETL workflow, and stores it in a data warehouse designed using a star schema for analytical use.

---

## Objectives

* Build a fully functional ETL pipeline
* Implement layered data architecture (staging → warehouse)
* Design a star schema (fact + dimension tables)
* Ensure idempotent pipeline execution
* Enable business-driven analytics

---

## Architecture

API → Python (Extract) → Staging Layer → Transformation Layer → Data Warehouse → Analytics

---

## Tech Stack

* Python
* SQL Server
* pyodbc
* REST API
* T-SQL

---

## Pipeline Workflow

### 1. Extract

* Fetches product data from API
* Saves data as JSON (`products_latest.json`)
* Includes logging and validation

### 2. Load

* Loads data into staging table (`stg_products`)
* Implements incremental logic (avoids duplicates)

### 3. Transform

* Builds star schema:

  * `dim_product`
  * `fact_product_sales`
* Applies transformation and modeling logic

### 4. Orchestration

* Entire pipeline executed via:

```bash
py run_pipeline.py
```

---

## Data Model

### 🔹 Staging Layer

* `stg_products`

### 🔹 Dimension Table

* `dim_product`

  * product_id
  * title
  * category

### 🔹 Fact Table

* `fact_product_sales`

  * product_id
  * price
  * quantity
  * total_amount

---

##  Business Questions & Analysis

### 1. Which product categories generate the highest revenue?

```sql
SELECT 
    p.category,
    SUM(f.total_amount) AS revenue
FROM fact_product_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;
```

**Result:**

| Category   | Revenue    |
| --------   | ---------  |
| furniture  |	11299,89  |
| fragrances | 	1619,81   |
| groceries  |	252,16    |
| Beauty     |  214,85    | 

---

### 2. How many products are sold per category?

```sql
SELECT 
    p.category,
    COUNT(*) AS total_products_sold
FROM fact_product_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_products_sold DESC;
```

**Result:**

| Category   | Total Products Sold |
| --------   | ------------------- |
| groceries  |  15                 |
| Beauty     |   5                 |
| fragrances |   5                 |
| furniture  |   5                 |

---

### 3. What is the average order value per category?

```sql
SELECT 
    p.category,
    AVG(f.total_amount) AS avg_order_value
FROM fact_product_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY avg_order_value DESC;
```

**Result:**

| Category | Avg Order Value |
| -------- | --------------- |
|furniture |	2259,978     |
|fragrances|	323,962	     |
|beauty	   |      42,97      |
|groceries |16,8106666666667 | 

---

### 4. Top 5 products by revenue

```sql
SELECT TOP 5
    p.title,
    SUM(f.total_amount) AS revenue
FROM fact_product_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.title
ORDER BY revenue DESC;
```

**Result:**


| Product                         	    | Revenue |
| ----------------------------------------- | ------- |
| Annibale Colombo Bed	          	    | 3799,98 |
| Wooden Bathroom Sink With Mirror	    | 3199,96 |
| Annibale Colombo Sofa	          	    | 2499,99 |
| Knoll Saarinen Executive Conference Chair | 1499,97 |
| Chanel Coco Noir Eau De		    |  649,95 | 

---

##  Data Validation

```sql
SELECT COUNT(*) FROM stg_products;
SELECT COUNT(*) FROM dim_product;
SELECT COUNT(*) FROM fact_product_sales;
```

**Expected Result:**

* stg_products: 30 rows
* dim_product: 30 rows
* fact_product_sales: 30 rows

---

## Key Features

* End-to-end ETL pipeline
* Star schema data modeling
* Incremental data loading
* Idempotent execution (safe reruns)
* Logging and error handling
* Modular and scalable design

---

##  What This Project Demonstrates

* Practical data engineering skills
* ETL pipeline design and implementation
* Data warehouse modeling (Kimball methodology)
* SQL-based analytics
* Handling real-world issues (duplicates, consistency)

---

## Future Improvements

* Implement dbt for transformations
* Add orchestration with Airflow or Azure Data Factory
* Integrate Azure Data Lake
* Add CI/CD pipeline
* Implement data quality tests

---

## Author

Panna Desai

