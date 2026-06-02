import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide")
st.title("📊 Superstore Sales Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")
    df["Order Date"] = pd.to_datetime(df["Order Date"], format='mixed', dayfirst=False)
    return df

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Data")
region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["Order Date"].min(), df["Order Date"].max()]
)

# --- APPLY FILTERS ---
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Order Date"] >= pd.to_datetime(date_range[0])) &
    (df["Order Date"] <= pd.to_datetime(date_range[1]))
]

# --- METRICS ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.0f}")
col3.metric("Total Orders", f"{filtered_df['Order ID'].nunique():,}")

# --- CHARTS ---
st.subheader("Sales by Category")
fig = px.bar(filtered_df.groupby("Category")["Sales"].sum().reset_index(),
             x="Category", y="Sales", color="Category")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Monthly Sales Trend")
filtered_df["Month"] = filtered_df["Order Date"].dt.to_period("M").astype(str)
monthly = filtered_df.groupby("Month")["Sales"].sum().reset_index()
fig2 = px.line(monthly, x="Month", y="Sales", markers=True)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Raw Data")
st.dataframe(filtered_df)