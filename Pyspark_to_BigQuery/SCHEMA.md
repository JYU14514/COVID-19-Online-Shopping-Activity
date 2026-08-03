### BigQuery Data Schema (`amazon_analysis.fact_reviews_*`)

| Field Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| **`product_id`** | `STRING` | The unique Amazon Standard Identification Number (ASIN) for the product being reviewed. | `"B001E4KFG0"` |
| **`review_id`** | `STRING` | A unique alphanumeric identifier for the specific customer review. | `"R3O9SGZBVQG916"` |
| **`main_category`** | `STRING` | The top-level product category used for partitioning and mix-shift analysis. | `"Grocery & Gourmet Food"` |
| **`rating`** | `INTEGER` | The customer's product score on a 1 to 5 star scale. | `5` |
| **`review_text`** | `STRING` | The raw text submitted by the customer detailing their product experience. | `"Great product, but shipping took three weeks due to lockdowns."` |
| **`review_date`** | `DATE` | The exact calendar date the review was published on the platform. | `2020-04-15` |
| **`review_year`** | `INTEGER` | An engineered feature extracting the year from `review_date` to support macro volume trending. | `2020` |
| **`pandemic_phase`** | `STRING` | An engineered categorical bucket dividing the timeline into three distinct pandemic impact phases. | `"2_Lockdown"` |
| **`review_length`** | `INTEGER` | An engineered metric counting the total number of characters in the `review_text` to measure customer effort. | `248` |
| **`sentiment_score`** | `FLOAT` | An engineered numeric proxy evaluating the emotional tone of the review text (typically scaled from -1.0 to 1.0). | `-0.45` |
| **`has_shipping_keyword`** | `BOOLEAN` | An engineered flag identifying if the `review_text` contains supply chain friction keywords (e.g., "shipping", "delayed"). | `true` |
| **`helpful_vote`** | `INTEGER` | The total number of upvotes the review received from other community members, used to measure reliance on peer validation. | `14` |