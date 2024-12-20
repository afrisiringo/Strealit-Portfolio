import streamlit as st

# Data manipulation
import pandas as pd
import numpy as np

# Data viz
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# SQL query
import duckdb as db

# SQL function
def sql(sql_query):
    return db.sql(sql_query).to_df()

st.title("Black Pearl Coffee Shop Sales", anchor=False)

# --- BACKGROUND ---

# Menjelaskan fungsi dari link GitHub dengan HTML
st.markdown("<i>Click the GitHub icon below to view the Jupyter notebook source code for this project:</i>", unsafe_allow_html=True)

# Menambahkan link ke GitHub dengan ikon
st.markdown(
    "[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]"
    "(https://github.com/afrisiringo/Black-Pearl-Coffee-Shop-Sales-Analysis/blob/main/Sales_Analysis.ipynb)",
    unsafe_allow_html=True
)

st.markdown("---")


st.markdown("""
### Background
<p style='text-align: justify; padding: 1px;'>
Black Pearl is a newly opened coffee shop with a pirate theme that operates in three locations: X, Y, and Z. 
The company offers a variety of coffee, tea, and drinking chocolate products. 
This project analyzes sales data from each location for the first semester of 2023 to provide insights into customer behavior and preferences, 
with the goal of supporting business growth and development.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- OBJECTIVE

st.markdown("""
### Objective
<p style='text-align: justify; padding: 1px;'>
To derive insights that can help Black Pearl coffee shop optimize sales and improve product offerings.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- PROBLEM STATEMENT ---

st.markdown("""
### Problem Statement
<ul style='text-align: justify; padding: 10px;'>
<li>What are the best-selling products and categories?</li>
<li>How do sales compare across the three locations?</li>
<li>Are there seasonal or time-based trends in sales?</li>
<li>What is the sales projection for next semester?</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("---")

# --- DATASET ---

@st.cache_resource
def load_data():
    filepath = r"C:\Users\sirin\OneDrive\Desktop\MyStreamlitPorto\Strealit-Portfolio\assets\Black_Pearl_Sales.xlsx"
    return pd.read_excel(filepath)

sales = load_data()

st.markdown("""
### Dataset
<p style='text-align: justify; padding: 1px;'>
The data used is sales data for 6 months from a coffee shop that just started operating in early January 2023. 
</p>
""", unsafe_allow_html=True)

# Menampilkan DataFrame di Streamlit
st.dataframe(sales)

st.markdown("---")

# --- DATA PREPARATION ---

sales['transaction_time'] = pd.to_datetime(sales['transaction_time'], format='%H:%M:%S')

# Revenue
sales["revenue"] = sales["transaction_qty"] * sales["unit_price"]

# The hour of the transactions
sales["transaction_hour"] = sales["transaction_time"].dt.hour

# Name of the day
sales["day_of_week"] = sales["transaction_date"].dt.day_name()

# --- Top 10 Best Selling Items ---
st.markdown("""
### Top 10 Best Selling Items
<p style='text-align: justify; padding: 1px;'>
The best-selling item is Earl Grey Rg, with a total of 4,708 units sold, making it the most popular choice among buyers. 
Note that the differences in the number of units sold for each product are not significant.
</p>
""", unsafe_allow_html=True)

best_selling = sql(
    """
    SELECT 
        product_detail,
        SUM(transaction_qty) as total_sold
    FROM sales
    GROUP BY product_detail
    ORDER BY SUM(transaction_qty) DESC
    LIMIT 10
    """
)

# Data viz with horizontal bar chart
fig = px.bar(
    best_selling, 
    x="total_sold", 
    y="product_detail", 
    orientation='h',
    color="product_detail",
    hover_name="product_detail"
)

# Custom layout
fig.update_layout(
    width=1200,
    xaxis_title="Total Units Sold",
    yaxis_title="",
    showlegend=False
)

# Menampilkan grafik di Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- 10 Top Earner Items ---

st.markdown("""
### Top Earner Items
<p style='text-align: justify; padding: 1px;'>
Interestingly, although Earl Grey Rg is the best-selling item, it is not the item that generates the most revenue. The top earner is Davy Jones Hot Chocolate Lg, generating total sales 
of $21,151.75 , making it the highest revenue-generating item based on sales, followed by Jolly Roaster's Dark Chocolate Lg with a slight difference with a value of $21,006 .
</p>
""", unsafe_allow_html=True)

# Query
top_earner = sql(
    """
    SELECT 
        product_detail,
        SUM(revenue) as total_revenue
    FROM sales
    GROUP BY product_detail
    ORDER BY SUM(revenue) DESC
    LIMIT 10
    """
)

# Data viz with horizontal bar chart
fig = px.bar(
    top_earner, 
    x="total_revenue", 
    y="product_detail", 
    orientation='h',
    color="product_detail",
    hover_name="product_detail"
)

# Custom layout
fig.update_layout(
    width=1200,
    xaxis_title="Total Sales ($)",
    yaxis_title="",
    xaxis=dict(tickformat=","),
    showlegend=False
)

# Menampilkan grafik di Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- Total Sales by Product Category ---

st.markdown("""
### Total Sales by Product Category
<p style='text-align: justify; padding: 1px;'>
The coffee product category generated a revenue of $269,952.45, making it the top earner. This figure makes sense, as the shop primarily focuses on coffee. The sales reflect the demand for 
coffee among customers, aligning with the shop's core offerings.
</p>
""", unsafe_allow_html=True)

# Query
sales_by_category = sql(
    """
    SELECT 
        product_category,
        SUM(revenue) AS total_sales
    FROM sales
    GROUP BY product_category
    ORDER BY SUM(revenue) DESC
    """
)

# Data viz with horizontal bar chart
fig = px.bar(
    sales_by_category, 
    x="total_sales", 
    y="product_category", 
    orientation='h',
    color="product_category",
    hover_name="product_category"
)

# Custome layout
fig.update_layout(
    width=1200,
    xaxis_title="Total Sales ($)",
    yaxis_title="",
    xaxis=dict(tickformat=","),
    showlegend=False
)

# Menampilkan grafik di Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- Total Sales By Locations ---

st.markdown("""
### Total Sales by Store Locations
<p style='text-align: justify; padding: 1px;'>
The Coffee Shop in location Y has generated the highest revenue. However, it's important to note that the financial performance across all three locations is quite similar, as the differences in total sales 
among them are not significant.
</p>
""", unsafe_allow_html=True)

sales_by_locations = sql(
    """
    SELECT
        store_location,
        SUM(revenue) AS total_sales
    FROM sales
    GROUP BY store_location
    ORDER BY SUM(revenue) DESC
    """
)

# Data viz with horizontal bar chart
fig = px.bar(
    sales_by_locations, 
    x="store_location", 
    y="total_sales", 
    color="store_location",
    hover_name="store_location"
)

# Custome layout
fig.update_layout(
    width=1200,
    xaxis_title="Total Sales ($)",
    yaxis_title="",
    xaxis=dict(tickformat=","),
    showlegend=False
)

# Menampilkan grafik di Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- Distribution of Total Sales Per Hour: Peak Sales Times ---

st.markdown("""
### Distribution of Total Sales Per Hour: Peak Sales Times
""", unsafe_allow_html=True)

# Query
hourly_rev = sql(
    """
    SELECT 
        DAYOFWEEK(transaction_date) AS day,
        day_of_week,
        transaction_hour,
        SUM(revenue) AS total_sales
    FROM sales
    GROUP BY 
        DAYOFWEEK(transaction_date),
        day_of_week,
        transaction_hour
    ORDER BY 
        DAYOFWEEK(transaction_date),
        transaction_hour
    """
)

pivot_df = hourly_rev.pivot(index="day_of_week", columns="transaction_hour", values="total_sales")

days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Sort the names of the days
pivot_df = pivot_df.reindex(days_order)

# Membuat heatmap dengan Plotly
fig = px.imshow(pivot_df, 
                text_auto=True, 
                labels=dict(x="Hour of The Day", y="", color="Total Sales"), 
                color_continuous_scale='YlGnBu',
                width=1200)

# Menonaktifkan color bar
fig.update_layout(
    coloraxis_showscale=False
)

# Menampilkan grafik di Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<p style='text-align: justify; padding: 1px;'>
From the heatmap we can see a few key insights:
</p> 
<ul style='text-align: justify; padding: 10px;'>       
<li>Black Pearl Coffee Shop is always open every day of the week.</li>
<li>Sales tend to peak around 7 AM to 11 AM. This suggests high customer traffic during typical breakfast hours.</li>
<li>There's a noticeable decline in sales at 8 PM, which are significantly lower than during peak hours, with an average of $419.38 and a total of $2,935.64.</li>
</ul>
<p style='text-align: justify; padding: 1px;'>
Due to the low revenue at 8 PM, it might be a good idea to close the coffee shop at this time instead of staying open later. This could cut down on costs like staff wages and utilities when 
there aren't enough sales to cover them. Additionally, adjusting the hours could help manage staff better and improve service during the busier times, which might increase profits.
</p> 
""", unsafe_allow_html=True)

st.markdown("---")

# --- Sales Trend ---

st.markdown("""
### Sales Trend
""", unsafe_allow_html=True)

# Query
sales_trend = sql(
    """
    SELECT 
        transaction_date,
        SUM(revenue) as sales
    FROM sales
    GROUP BY transaction_date
    ORDER BY transaction_date ASC
    """
)

# Make a time series data frame
sales_trend = sales_trend.set_index('transaction_date')

# Set the frequency to daily
sales_trend = sales_trend.asfreq('D')

# Data viz of sales trend
fig = px.line(sales_trend, x=sales_trend.index, y="sales")
fig.update_layout(
    width=1200,
    height=500,
    xaxis_title='',
    yaxis_title='Sales ($)'
)

# Menampilkan grafik di Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<ul style='text-align: justify; padding: 10px;'>       
<li>The sales have an upward trend. This trend shows a slow but consistent increase in sales over time. This indicates that, overall, there was growth in sales during this period, despite daily fluctuations.</li>
<li>Sales have a seasonality component where sales will drop quite drastically at the end of each month and increase slightly at the beginning of the month.</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Time Series Analysis: Sales Projection ---

st.markdown("""
### Time Series Analysis: Sales Projection
""", unsafe_allow_html=True)

# Load data dari kedua file CSV
original_sales_df = pd.read_csv(r"C:\Users\sirin\OneDrive\Desktop\MyStreamlitPorto\Strealit-Portfolio\assets\original_sales.csv")
forecast_sales_df = pd.read_csv(r"C:\Users\sirin\OneDrive\Desktop\MyStreamlitPorto\Strealit-Portfolio\assets\sales_forecast.csv")

# Membuat line graph
fig = go.Figure()

# Menambahkan line untuk original sales
fig.add_trace(go.Scatter(x=original_sales_df['transaction_date'], y=original_sales_df['sales'], 
                         mode='lines', name='Original Sales', 
                         line=dict(color='blue')))

# Menambahkan line untuk forecast sales
fig.add_trace(go.Scatter(x=forecast_sales_df['transaction_date'], y=forecast_sales_df['sales'], 
                         mode='lines', name='Forecast Sales', 
                         line=dict(color='red')))

# Update layout
fig.update_layout(
     xaxis_title="",
    yaxis_title="Sales ($)",
)

# Menampilkan grafik di Streamlit
st.plotly_chart(fig)

st.markdown("""
<p style='text-align: justify; padding: 1px;'>
From the analysis of the sales prediction graph using the Holt-Winters model, it appears there is a consistent upward trend in sales data. Based on predictions, sales will increase by 109.09% 
in the next semester. Plan promotions and marketing efforts to keep customers interested and engaged. Tailor promotions around observed peak times and customer preferences gathered from sales data.
</p> 
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: justify; padding: 1px;'>
<b><i>The results of this forecast show an optimistic upward trend, but the following points need to be noted:</i></b>
</p> 
<ul style='text-align: justify; padding: 10px;'>       
<li>The steady increase in sales might be due to initial interest as the coffee shop is new. This kind of trend is common with new establishments as they attract initial curiosity and visits from potential regulars.</li>
<li>With only six months of data, predicting long-term trends can be unreliable. Early data from new businesses might not fully capture cyclical trends or the effect of external factors like seasonality and market competition.</li>
<li>The model might be overly optimistic due to the short amount of data available. This can cause it to not accurately predict future changes, such as potential decreases in sales once the initial excitement of the coffee shop's opening fades.</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Recomendation ---

st.markdown("""
### Recomendation
<p style='text-align: justify; padding: 1px;'>
<b>Business Strategy Adjustments:</b>
</p> 
<ul style='text-align: justify; padding: 10px;'>
<li><b><i>Promotional Activities:</i></b> Plan promotions and marketing efforts to keep customers interested and engaged. Tailor promotions around observed peak times and customer preferences</li>
<li><b><i>Operational Planning:</i></b> Prepare for potential high-traffic periods by optimizing staffing and inventory based on forecasted sales peaks.</li>
<li><b><i>Early Close:</i></b> Due to the low revenue at 8 PM, it might be a good idea to close the coffee shop at this time instead of staying open later.</li>
</ul>
<p style='text-align: justify; padding: 1px;'>
<b>Data Collection:</b>
</p> 
<ul style='text-align: justify; padding: 10px;'>
<li><b><i>Data Duration:</i></b> Aim to collect at least one to two years of data. This duration will help capture a wider range of seasonal variations and customer behavior patterns.</li>
<li><b><i>Diversify Data Sources:</i></b> Start incorporating data on local events, weather conditions, and economic indicators which might influence customer purchasing behavior.</li>
<li><b><i>Customer Feedback:</i></b> Regularly gather customer feedback to understand preferences and dissatisfaction points, which can be crucial for adjusting business strategies.</li>
</ul>
""", unsafe_allow_html=True)