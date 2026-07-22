from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import warnings

# Suppress minor matplotlib warnings for cleaner terminal output
warnings.filterwarnings("ignore")

print("Querying BigQuery and generating report. This may take a moment...")

# Initialize the BigQuery client (Cloud Shell authenticates automatically)
client = bigquery.Client(project="project-4dd1cf45-07ac-448f-839")

# Pull the aggregated metrics across all 7 categories using a wildcard
query = """
        SELECT
            main_category,
            review_year,
            pandemic_phase,
            COUNT(*) as total_volume,
            AVG(review_length) as avg_length,
            AVG(sentiment_score) as avg_sentiment,
            AVG(CAST(has_shipping_keyword AS INT64)) as pct_shipping_kw,
            AVG(helpful_vote) as avg_helpful
        FROM `project-4dd1cf45-07ac-448f-839.amazon_analysis.fact_reviews_*`
        GROUP BY main_category, review_year, pandemic_phase
        ORDER BY review_year \
        """

# Load data into a Pandas DataFrame
df = client.query(query).to_dataframe()

# Create the Final PDF Report
with PdfPages('amazon_reviews_comprehensive_report.pdf') as pdf:

    # 1. Macro Market Activity Shift
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    df_vol = df.groupby('review_year')['total_volume'].sum().reset_index()
    ax1.plot(df_vol['review_year'], df_vol['total_volume'], marker='o', color='#2c3e50')
    ax1.axvspan(2020, 2021, color='#e74c3c', alpha=0.2, label='Lockdown Phase')
    ax1.set_title("1. Macro Market Activity Shift")
    ax1.set_ylabel("Total Reviews")
    ax1.legend()
    pdf.savefig(fig1)
    plt.close(fig1)

    # 2. Category Mix Shift (Share of Total Reviews)
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    df_mix = df.groupby(['pandemic_phase', 'main_category'])['total_volume'].sum().unstack()
    df_mix_pct = df_mix.div(df_mix.sum(axis=1), axis=0) * 100
    df_mix_pct = df_mix_pct.loc[["1_Pre-COVID", "2_Lockdown", "3_New Normal"]]
    df_mix_pct.plot(kind='bar', stacked=True, ax=ax2, colormap='Set2')
    ax2.set_title("2. Category Mix Shift (Share of Total Reviews)")
    ax2.set_ylabel("Percentage of Total Volume (%)")
    ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=0)
    pdf.savefig(fig2, bbox_inches='tight')
    plt.close(fig2)

    # 3. Emotional Tone & Customer Effort
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    phases = df['pandemic_phase'].unique()
    for p in phases:
        subset = df[df['pandemic_phase'] == p]
        ax3.scatter(subset['avg_length'], subset['avg_sentiment'], alpha=0.7, label=p)
    ax3.set_title("3. Emotional Tone & Customer Effort (Deliverable 5)")
    ax3.set_xlabel("Average Review Length")
    ax3.set_ylabel("Average Sentiment Score")
    ax3.legend()
    pdf.savefig(fig3)
    plt.close(fig3)

    # 4. Supply Chain Friction - Multi-Phase
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    df_ship = df.groupby('pandemic_phase')['pct_shipping_kw'].mean().reset_index()
    ax4.bar(df_ship['pandemic_phase'], df_ship['pct_shipping_kw'], color=['#3498db', '#e74c3c', '#2ecc71'])
    ax4.set_title("4. Supply Chain Friction - Multi-Phase (Deliverable 7)")
    ax4.set_ylabel("% of Reviews with Shipping Keywords")
    pdf.savefig(fig4)
    plt.close(fig4)

    # 5. Community Reliance
    fig5, ax5 = plt.subplots(figsize=(10, 5))
    df_help = df.groupby('review_year')['avg_helpful'].mean().reset_index()
    ax5.plot(df_help['review_year'], df_help['avg_helpful'], marker='s', color='#8e44ad')
    ax5.axvspan(2020, 2021, color='#e74c3c', alpha=0.2)
    ax5.set_title("5. Community Reliance & Validation (Deliverable 6)")
    ax5.set_ylabel("Avg Helpful Votes per Review")
    pdf.savefig(fig5)
    plt.close(fig5)

print("Success! Report saved locally as amazon_reviews_comprehensive_report.pdf")