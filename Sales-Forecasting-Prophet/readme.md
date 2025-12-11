#  Sales Forecasting with Facebook Prophet

## Project Overview

This project implements a Time Series Forecasting model using the **Facebook Prophet** library to predict future sales volume. The analysis leverages historical transactional data, with a focus on decomposing the time series into its core components: trend, weekly seasonality, yearly seasonality, and the impact of specific holidays.

The complete end-to-end workflow, from raw data extraction via SQL to model validation and visualization, is documented in the accompanying [Notebook .ipynb](Notebook%20.ipynb).

###  Objective

The primary goal is to generate reliable forecasts to support business operations, specifically for inventory planning and budget allocation:
1.  Forecast the daily sales quantity for a future period (e.g., the next 12 months).
2.  Quantify and visualize the individual contributions of trend and seasonality.
3.  Enhance forecast accuracy by incorporating external factors (holidays).

---

###  Technology Stack

| Category | Tools & Libraries | Purpose |
| :--- | :--- | :--- |
| **Data Sourcing** | SQL (Deepnote SQL Blocks) | Aggregating raw order and line-item data into a clean, daily time series (`ds` and `y` columns). |
| **Data Manipulation** | Python, Pandas | Data cleaning, time series preparation, and feature engineering. |
| **Modeling** | Facebook Prophet | Core forecasting engine, optimized for business data with strong seasonal patterns. |
| **Visualization** | Matplotlib | Plotting the forecast, components, and model diagnostics. |

---

###  Methodology and Analysis

#### 1. Data Preparation and SQL Aggregation
The sales data was sourced from an aggregated SQL query designed to calculate the total item quantity sold (`y`) for each day (`ds`). This step demonstrates competence in handling data from its source, not just importing pre-cleaned files:

```sql
-- Snippet from the core SQL query for generating the time series
SELECT 
    CAST(o.created_timestamp as DATE) AS ds,
    SUM(l.item_qty) as y
FROM orders.csv o
JOIN line_items.csv l ON o.id = l.order_id
GROUP BY 1

###  Model Configuration
The Prophet model (m) was configured specifically for this dataset:

Seasonality: Both Weekly and Yearly seasonality components were enabled due to observed short-term and long-term cyclic patterns.

Holidays: A custom dataframe of relevant business/national holidays was created and added to the model initialization. This is a critical step to ensure that predictable spikes/drops around major events are accounted for, improving robustness.

###  Key Findings
Strong Growth Trend: The data clearly exhibits a robust upward trend across the entire period, which the model projects to continue into the future.

High Volatility: The forecast plot shows significant short-term fluctuations, confirming the presence of strong weekly seasonality.

Uncertainty (Confidence Interval): The light blue shaded area (95% Confidence Interval) demonstrates the model's prediction uncertainty, which naturally widens as the forecast extends further into the future.
