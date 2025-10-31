"""
Streamlit Dashboard Template

Run with: streamlit run dashboard-template.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Business Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load data function
@st.cache_data
def load_data():
    # Replace with your data loading logic
    # df = pd.read_csv('data.csv')
    # For demo, create sample data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    df = pd.DataFrame({
        'date': dates,
        'revenue': np.random.randint(10000, 50000, len(dates)),
        'orders': np.random.randint(100, 500, len(dates)),
        'category': np.random.choice(['A', 'B', 'C'], len(dates))
    })
    return df

# Header
st.title("📊 Business Intelligence Dashboard")
st.markdown(f"**Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Sidebar filters
st.sidebar.header("Filters")
date_range = st.sidebar.date_input(
    "Date Range",
    value=(datetime.now() - timedelta(days=30), datetime.now())
)
category_filter = st.sidebar.multiselect(
    "Category",
    options=['All', 'A', 'B', 'C'],
    default=['All']
)
refresh_button = st.sidebar.button("Refresh Data")

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info("This dashboard provides real-time business intelligence metrics.")

# Load data
df = load_data()

# Apply filters
if 'All' not in category_filter and len(category_filter) > 0:
    df = df[df['category'].isin(category_filter)]

# KPI Cards
st.markdown("## Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_revenue = df['revenue'].sum()
    st.metric(
        label="Total Revenue",
        value=f"${total_revenue:,.0f}",
        delta="+15.3%"
    )

with col2:
    total_orders = df['orders'].sum()
    st.metric(
        label="Total Orders",
        value=f"{total_orders:,}",
        delta="+8.2%"
    )

with col3:
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
    st.metric(
        label="Avg Order Value",
        value=f"${avg_order_value:.2f}",
        delta="-2.1%",
        delta_color="inverse"
    )

with col4:
    conversion_rate = 3.45  # Calculate from your data
    st.metric(
        label="Conversion Rate",
        value=f"{conversion_rate:.2f}%",
        delta="+0.5%"
    )

st.divider()

# Main content
st.markdown("## Detailed Analysis")

# Two-column layout
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Revenue Trend")

    # Aggregate by date
    daily_revenue = df.groupby('date')['revenue'].sum().reset_index()

    fig_trend = px.line(
        daily_revenue,
        x='date',
        y='revenue',
        title='Daily Revenue'
    )
    fig_trend.update_layout(
        xaxis_title="Date",
        yaxis_title="Revenue ($)",
        hovermode='x unified'
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with col_right:
    st.subheader("Category Breakdown")

    category_revenue = df.groupby('category')['revenue'].sum().reset_index()

    fig_pie = px.pie(
        category_revenue,
        names='category',
        values='revenue',
        title='Revenue by Category'
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.divider()

# Full-width chart
st.subheader("Orders Over Time")
daily_orders = df.groupby('date')['orders'].sum().reset_index()

fig_orders = px.area(
    daily_orders,
    x='date',
    y='orders',
    title='Daily Orders'
)
fig_orders.update_layout(
    xaxis_title="Date",
    yaxis_title="Orders",
    hovermode='x unified'
)
st.plotly_chart(fig_orders, use_container_width=True)

st.divider()

# Detailed data table
st.subheader("Detailed Data")

# Add filters to table
search = st.text_input("Search", "")
if search:
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
else:
    filtered_df = df

st.dataframe(
    filtered_df.head(100),
    use_container_width=True,
    height=400
)

# Download button
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Data as CSV",
    data=csv,
    file_name=f"data_{datetime.now().strftime('%Y%m%d')}.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.caption("Data refreshed every 15 minutes | Source: Analytics Database | © 2025 Your Company")
