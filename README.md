# Superstore Sales Dashboard

Live Demo: https://superstore-dashboard-7fo5spcjsappufv5ywbzhui.streamlit.app

### **Project Overview**
Interactive sales analytics dashboard built to explore 4 years of Superstore retail data. Identifies trends, regional performance, and profitability drivers using Python.

### **Key Features**
- **Interactive Filters**: Region + Date Range selectors update all charts in real-time
- **KPI Metrics**: Total Sales, Profit, and Order count with dynamic calculations  
- **Data Visualizations**: Category sales bar chart + Monthly sales trend line chart
- **Raw Data Explorer**: Filtered dataset view for detailed analysis

### **Tech Stack**
- **Python**: Pandas for data manipulation, datetime handling
- **Visualization**: Plotly Express for interactive charts  
- **Dashboard**: Streamlit for web app framework + deployment
- **Deployment**: Streamlit Community Cloud

### **Skills Demonstrated**
1. Data cleaning and aggregation with Pandas `groupby()`
2. Time-series analysis using `pd.to_datetime()` and monthly resampling
3. Interactive dashboard development with Streamlit widgets
4. Data visualization best practices with Plotly
5. End-to-end project deployment and version control with Git/GitHub

### **How to Run Locally**
```bash
pip install -r requirements.txt
streamlit run app.py
