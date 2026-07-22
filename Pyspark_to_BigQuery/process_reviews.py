import sys
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, FloatType

# ==========================================
# 1. DYNAMIC CONFIGURATION
# ==========================================
# Ensure a category argument was passed when the job was submitted
if len(sys.argv) < 2:
    print("Error: Please provide a category name (e.g., All_Beauty)")
    sys.exit(1)

category_name = sys.argv[1]

# Initialize Spark Session (Dataproc handles the BigQuery connection natively)
spark = SparkSession.builder \
    .appName(f"Amazon_Reviews_ETL_{category_name}") \
    .getOrCreate()

# Cloud Storage and BigQuery paths dynamically update based on the category
gcs_bucket = "amazon-reviews-project-data"
gcp_project_id = "project-4dd1cf45-07ac-448f-839"

review_path = f"gs://{gcs_bucket}/raw_reviews/{category_name}.jsonl"
meta_path = f"gs://{gcs_bucket}/raw_metadata/meta_{category_name}.jsonl"

# Creates a dedicated table for each category (e.g., fact_reviews_all_beauty)
bq_dataset_table = f"{gcp_project_id}.amazon_analysis.fact_reviews_{category_name.lower()}"

# ==========================================
# 2. LOAD & JOIN DATA
# ==========================================
print(f"Loading data for category: {category_name}...")
df_reviews = spark.read.json(review_path).withColumnRenamed("title", "review_title")

meta_schema = StructType([
    StructField("parent_asin", StringType(), True),
    StructField("main_category", StringType(), True),
    StructField("title", StringType(), True)
])

df_meta_clean = spark.read.json(meta_path, schema=meta_schema) \
    .withColumnRenamed("title", "product_title") \
    .dropDuplicates(["parent_asin"])

df_joined = df_reviews.join(df_meta_clean, on="parent_asin", how="left")

# ==========================================
# 3. FEATURE ENGINEERING
# ==========================================
print("Applying feature engineering and timeline filters...")

df_final = df_joined \
    .withColumn("review_date", F.to_date(F.from_unixtime(F.col("timestamp") / 1000))) \
    .withColumn("review_year", F.year("review_date")) \
    .withColumn("year_month", F.date_format("review_date", "yyyy-MM")) \
    .filter((F.col("review_date") >= "1996-05-01") & (F.col("review_date") <= "2023-09-30")) \
    .withColumn("pandemic_phase",
                F.when(F.col("year_month") < "2020-03", "1_Pre-COVID")
                .when((F.col("year_month") >= "2020-03") & (F.col("year_month") <= "2021-02"), "2_Lockdown")
                .otherwise("3_New Normal")
                ) \
    .withColumn("review_length", F.length(F.col("text"))) \
    .withColumn("has_shipping_keyword", F.lower(F.col("text")).rlike("delay|shipping|arrived|customer service")) \
    .withColumn("sentiment_score", (F.col("rating") - 3) / 2.0) \
    .select(
    "review_date", "year_month", "review_year", "pandemic_phase",
    "parent_asin", "product_title", "main_category",
    "rating", "sentiment_score", "review_length", "has_shipping_keyword",
    "helpful_vote", "verified_purchase", "user_id", "review_title"
)

# ==========================================
# 4. WRITE DIRECTLY TO BIGQUERY
# ==========================================
print(f"Writing {category_name} directly to BigQuery: {bq_dataset_table}...")

# Dataproc Serverless natively supports the spark-bigquery-connector without staging
df_final.write \
    .format("bigquery") \
    .option("table", bq_dataset_table) \
    .option("writeMethod", "direct") \
    .mode("overwrite") \
    .save()

print(f"Pipeline complete for {category_name}!")