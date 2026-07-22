# COVID-19-Online-Shopping-Activity
Big Data Group 9 Project

# Amazon Reviews Pandemic Impact Analysis

## Project Overview
This repository contains the data engineering pipeline and analysis scripts for a master's project evaluating macro market activity shifts surrounding the 2020 COVID-19 pandemic lockdowns. The project analyzes a dataset of tens of millions of Amazon consumer reviews spanning from **May 1996 to September 2023**.

The pipeline utilizes **Google Cloud Storage (GCS)** as the foundational raw data lake, processes the data using scalable PySpark jobs on **Google Cloud Dataproc Serverless**, and stages the final structured data in **Google Cloud BigQuery** for reporting and visualization in **Tableau**.

## Architecture & Tech Stack
* **Raw Storage:** Google Cloud Storage (GCS)
* **Compute / Data Engineering:** Google Cloud Dataproc Serverless (PySpark)
* **Data Warehouse:** Google Cloud BigQuery
* **Reporting / Analytics:** Python (Pandas, Matplotlib)
* **Business Intelligence:** Tableau Desktop

---

## Prerequisites
Before running the pipeline, ensure the following Google Cloud environment configurations are met:

1. **Google Cloud Project Setup:**
    * Project ID: `project-4dd1cf45-07ac-448f-839`
    * Region: `us-central1`
2. **APIs Enabled:**
    * Compute Engine API
    * Dataproc API
    * BigQuery API
3. **IAM Permissions:**
   The default Compute Engine Service Account must have the **BigQuery Data Editor** role to allow PySpark to write outputs to BigQuery.
   ```bash
   # Fetch internal Project Number
   PROJECT_NUMBER=$(gcloud projects describe project-4dd1cf45-07ac-448f-839 --format="value(projectNumber)")
   
   # Grant Data Editor Role
   gcloud projects add-iam-policy-binding project-4dd1cf45-07ac-448f-839 \
       --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
       --role="roles/bigquery.dataEditor"
   
