import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat data
df = pd.read_csv('main_data.csv')
geolocation = pd.read_csv('geolocation.csv')

# Menghapus nilai NaN 
df = df.dropna(subset=['order_purchase_timestamp'])
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

st.title("Data Analytics Project: E-Commerce Public Dataset")

# Sidebar
st.sidebar.image("data_analytic.jpg", use_column_width=True)
st.sidebar.title("Data Analytic")

# Sidebar Filters
selected_year = st.sidebar.multiselect(
    "Select Year",
    options=df['order_purchase_timestamp'].dt.year.unique(),
    default=df['order_purchase_timestamp'].dt.year.unique()
)
selected_state = st.sidebar.multiselect(
    "Select State",
    options=df['customer_state'].unique(),
    default=df['customer_state'].unique()
)

# Filter Data
df_filtered = df[
    (df['order_purchase_timestamp'].dt.year.isin(selected_year)) &
    (df['customer_state'].isin(selected_state))
]

# Revenue Analysis
df_filtered['order_purchase_month'] = df_filtered['order_purchase_timestamp'].dt.to_period('M')
revenue_by_month = df_filtered.groupby('order_purchase_month')['payment_value'].sum().reset_index()

st.title("Revenue Analysis")
st.line_chart(data=revenue_by_month, x='order_purchase_month', y='payment_value')

# Orders by Location
location_data = pd.merge(df, geolocation, left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix')
location_orders = location_data.groupby(['geolocation_city', 'geolocation_state']).size().reset_index(name='total_orders')
top_locations = location_orders.sort_values('total_orders', ascending=False).head(10)
top_locations['Location'] = top_locations['geolocation_city'] + ', ' + top_locations['geolocation_state']

st.title("Top 10 Locations by Orders")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_locations, y='Location', x='total_orders', palette='coolwarm', ax=ax)
ax.set_title("Top 10 Locations by Orders")
ax.set_xlabel("Total Orders")
ax.set_ylabel("Location")
st.pyplot(fig)

# Sales per Product Category
product_sales = df.groupby('product_category_name_english').size().reset_index(name='total_sales')
top_categories = product_sales.sort_values('total_sales', ascending=False).head(10)

st.title("Top 10 Product Categories by Sales")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_categories, y='product_category_name_english', x='total_sales', palette='rocket', ax=ax)
ax.set_title("Top 10 Product Categories by Sales")
ax.set_xlabel("Total Sales")
ax.set_ylabel("Product Category")
st.pyplot(fig)

st.caption('Copyright (C) Yogik Septiadi 2024')