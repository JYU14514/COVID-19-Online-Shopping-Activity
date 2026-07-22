## Steps to upload files to GCS:

#### 1. Launch a VM Instance
#### 2. Use Screen to ensure running on background.
````
# To create new screen:
screen -S <screen_name>

# To dettach from current screen:
screen -d

# To reattach to previous screen:
screen -r <screen_name>

# Document: https://linuxize.com/post/how-to-use-linux-screen/
````

#### 3. In VM instance, upload data to GCS

Reviews:
````
curl https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Video_Games.jsonl.gz \
| pigz -dc \
| gsutil cp - gs://amazon-reviews-project-data/raw_reviews/Video_Games.jsonl
````
Metadata:
````
curl https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Video_Games.jsonl.gz \
| pigz -dc \
| gsutil cp - gs://amazon-reviews-project-data/raw_metadata/meta_Video_Games.jsonl
````
## Steps to Process data & Store to BigQuery:

#### 1. Create new table in BigQuery

#### 2. Upload script [process_reviews.py](process_reviews.py) to GCS

#### 3. Run script in GC terminal
````
gcloud dataproc batches submit pyspark gs://amazon-reviews-project-data/scripts/process_reviews.py \
--batch="video-games-1" \
--project="project-4dd1cf45-07ac-448f-839" \
--region="us-west1" \
--subnet="default" \
-- Video_Games
````