Commands to upload files to GCS:

1. Launch GC Shell;
````
wget <link>;

gunzip <gz file>;

gcloud storage cp <jsonl file> gs://<your-bucket-name>/raw_reviews/

````


````
curl https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Grocery_and_Gourmet_Food.jsonl.gz \
| pigz -dc \
| gsutil cp - gs://amazon-reviews-project-data/raw_reviews/Grocery_and_Gourmet_Food.jsonl
````