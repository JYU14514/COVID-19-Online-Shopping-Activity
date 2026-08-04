SELECT
    pandemic_phase,
    COUNT(*) AS review_count,
    AVG(rating) AS avg_rating,
    AVG(sentiment_score) AS avg_sentiment_score,
    AVG(review_length) AS avg_review_length,
    SAFE_DIVIDE(COUNTIF(has_shipping_keyword = true), COUNT(*)) * 100 AS pct_shipping_keyword,
    SAFE_DIVIDE(COUNTIF(verified_purchase = true), COUNT(*)) * 100 AS pct_verified_purchase,
    AVG(helpful_vote) AS avg_helpful_votes,
    COUNT(DISTINCT parent_asin) AS unique_products,
    COUNT(DISTINCT user_id) AS unique_users
FROM
    `project-4dd1cf45-07ac-448f-839.amazon_analysis.*`
WHERE
    review_year BETWEEN 2016 AND 2022
GROUP BY
    pandemic_phase
ORDER BY
    pandemic_phase;



SELECT
    pandemic_phase,
    main_category,
    COUNT(*) AS review_count,
    SAFE_DIVIDE(COUNT(*), SUM(COUNT(*)) OVER(PARTITION BY pandemic_phase)) * 100 AS category_share_pct,
    AVG(rating) AS avg_rating
FROM
    `project-4dd1cf45-07ac-448f-839.amazon_analysis.*`
WHERE
    review_year BETWEEN 2016 AND 2022
GROUP BY
    pandemic_phase,
    main_category
ORDER BY
    pandemic_phase,
    category_share_pct DESC;

SELECT
    review_year,
    COUNT(*) AS review_count
FROM
    `project-4dd1cf45-07ac-448f-839.amazon_analysis.*`
GROUP BY
    review_year
ORDER BY
    review_year;