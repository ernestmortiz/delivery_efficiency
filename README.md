# delivery_efficiency
An end-to-end analysis of food delivery operational data. This project uses Python and pandas for data cleaning and feature engineering, and a Google Sheets dashboard to visualize KPIs and provide actionable recommendations for improving delivery efficiency.

Delivery Operations Analysis & Change Management Proposal

Overview
This is a portfolio project demonstrating an end-to-end analytical workflow, from raw data processing to a strategic business recommendation. The project analyzes a dataset of ~200,000 food delivery orders to identify key drivers of delivery time and proposes a data-driven change management initiative to improve operational efficiency.

The goal is to showcase skills in data cleaning, feature engineering, dashboarding, and most importantly, translating raw data into actionable business insights.

Problem Statement
An operations manager at a delivery marketplace company needs to understand why some deliveries take longer than others. They need a clear, concise dashboard that not only tracks performance but also identifies the root causes of inefficiency so they can take targeted action to improve the customer and partner experience.

Tools & Technologies
Data Cleaning & Analysis: Python (pandas, NumPy)

Dashboarding & Visualization: Google Sheets

Methodology
The project was executed in three main steps:

1. Data Cleaning & Feature Engineering
The initial raw dataset contained missing values, impossible data points (e.g., negative numbers for on-shift partners), and raw timestamps. A Python script was used to:

Clean and validate the data.

Handle missing values using median and mode imputation.

Engineer two critical new features for analysis:

delivery_duration_minutes: The total time from order creation to actual delivery.

partner_utilization_rate: The ratio of busy partners to on-shift partners at the time of an order, created to measure supply-side strain.

2. Dashboarding in Google Sheets
The cleaned and enriched dataset was used to build a one-page executive dashboard in Google Sheets. The dashboard provides a clear, at-a-glance view of operational performance, featuring:

Headline KPIs: Average Delivery Time, Total Orders, and Average Partner Utilization.

Performance by Category: A bar chart identifying the store categories with the longest average delivery times.

Utilization Impact Analysis: A chart showing the direct relationship between high partner utilization and increased delivery durations.

3. Insights & Recommendations
The analysis of the dashboard yielded a clear, actionable insight that forms the basis for a strategic recommendation.

Insight:
Analysis of the delivery data reveals a direct correlation between high partner utilization and increased delivery times. When more than 85% of on-shift partners are busy with orders, the average delivery duration for customers increases significantly. This issue is most pronounced for our highest-volume categories, Pizza and American restaurants, which consistently experience the longest delivery times. This indicates that the operational bottleneck is a predictable supply-and-demand issue, occurring during peak hours when the number of available delivery partners is insufficient to meet customer order volume.

Data-Driven Action:
Based on these findings, a targeted change management initiative is recommended to address partner supply during these critical periods. The proposal is to launch a pilot program testing driver incentives in our top three busiest markets. This program would be active during the 6 PM to 9 PM window and focus on increasing the number of on-shift partners available for deliveries from Pizza and American restaurants. The success of this change will be measured by tracking the direct impact on delivery_duration_minutes in the test markets, with the goal of improving the customer experience without negatively impacting profitability.

Final Dashboard
A snapshot of the one-page dashboard summarizing key performance indicators and visualizations.

How to Run This Project
1. Ensure you have Python and the pandas library installed.
2. Place the raw dataset.csv file in the root directory.
3. Run the Python script to perform the cleaning and feature engineering. This will generate cleaned_delivery_data.csv.
4. Open cleaned_delivery_data.csv in Google Sheets to view the data used for the dashboard.
