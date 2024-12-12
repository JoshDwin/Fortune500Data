"""
Name: Joshua Dwinell
CS230: 2
Data: Fortune 500 Data
URL: Link to your web application on Streamlit Cloud (if posted)

Description: This program creates a website that shows many important information from the Fortune 500 data.
It shows top 10 graphs for many important pieces of data such as revenue, revenue per employee, employee count, and more.
It also includes a map and sliders and dropdowns to filter the data by state, revenue, and employee count.

"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
@st.cache_data
def load_data():
    file_path = "fortune_500_hq.xlsx"
    df = pd.read_excel(file_path)
    return df

df = load_data()

# Handle Missing Data
df.fillna({"REVENUES": 0, "EMPLOYEES": 1, "PROFIT": 0, "LATITUDE": 0, "LONGITUDE": 0}, inplace=True)
df.dropna(subset=["NAME", "STATE"], inplace=True)

# Preprocess Data
df["REVENUE_PER_EMPLOYEE"] = df["REVENUES"] / df["EMPLOYEES"]
df["STATE"] = df["STATE"].str.upper()

# Sidebar
st.sidebar.title("Filter Options")
state_filter = st.sidebar.multiselect("Filter by States:", options=sorted(df["STATE"].dropna().unique()), default=None)
if state_filter:
    df = df[df["STATE"].isin(state_filter)]

revenue_range = st.sidebar.slider("Filter by Revenue ($M):", min_value=0, max_value=int(df["REVENUES"].max()), value=(0, int(df["REVENUES"].max())))
df = df[(df["REVENUES"] >= revenue_range[0]) & (df["REVENUES"] <= revenue_range[1])]

employee_range = st.sidebar.slider("Filter by Employee Count:", min_value=0, max_value=int(df["EMPLOYEES"].max()), value=(0, int(df["EMPLOYEES"].max())))
df = df[(df["EMPLOYEES"] >= employee_range[0]) & (df["EMPLOYEES"] <= employee_range[1])]

# Add Download Button
st.sidebar.download_button(
    label="Download Filtered Data as CSV",
    data=df.to_csv(index=False),
    file_name="filtered_fortune_500_data.csv",
    mime="text/csv",
)

# Main Page Title
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f9;
        }
        .main {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-family: 'Arial', sans-serif;
            color: #2e77d0;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">Fortune 500 Insights</div>', unsafe_allow_html=True)
st.write("Explore interactive visualizations and detailed insights from Fortune 500 companies.")

# Key Metrics
total_revenue = df["REVENUES"].sum()
total_employees = df["EMPLOYEES"].sum()
avg_revenue_per_company = df["REVENUES"].mean()
top_company = df.loc[df["REVENUES"].idxmax(), "NAME"]

st.subheader("Key Metrics")

st.markdown(
    f"""
    <div style="display: flex; justify-content: space-between; text-align: center;">
        <div><b>Total Revenue ($M):</b> {total_revenue:,.2f}</div>
        <div><b>Total Employees:</b> {total_employees:,}</div>
        <div><b>Average Revenue per Company ($M):</b> {avg_revenue_per_company:,.2f}</div>
        <div><b>Top Revenue Company:</b> {top_company}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Graphs Section
st.header("Data Visualizations")

# Top 10 Companies by Revenue
st.subheader("Top 10 Companies by Revenue")
top_revenue = df.nlargest(10, "REVENUES")
fig_revenue = px.bar(
    top_revenue,
    x="REVENUES",
    y="NAME",
    orientation="h",
    title="Top 10 Companies by Revenue",
    labels={"REVENUES": "Revenue ($B)", "NAME": "Company"},
    color="REVENUES",
    color_continuous_scale="Blues",
)
st.plotly_chart(fig_revenue)

# Top 10 Companies by Employees
st.subheader("Top 10 Companies by Employees")
top_employees = df.nlargest(10, "EMPLOYEES")
fig_employees = px.bar(
    top_employees,
    x="EMPLOYEES",
    y="NAME",
    orientation="h",
    title="Top 10 Companies by Employees",
    labels={"EMPLOYEES": "Number of Employees", "NAME": "Company"},
    color="EMPLOYEES",
    color_continuous_scale="Greens",
)
st.plotly_chart(fig_employees)

# Top States by Company Count
st.subheader("Top States by Company Count")
state_counts = df["STATE"].value_counts().nlargest(10)
fig_states = px.bar(
    state_counts,
    x=state_counts.values,
    y=state_counts.index,
    orientation="h",
    title="Top 10 States by Company Count",
    labels={"y": "State", "x": "Company Count"},
    color=state_counts.values,
    color_continuous_scale="Viridis",
)
st.plotly_chart(fig_states)

# Revenue per Employee
st.subheader("Top 10 Companies by Revenue per Employee")
top_rev_per_emp = df.nlargest(10, "REVENUE_PER_EMPLOYEE")
fig_rev_per_emp = px.bar(
    top_rev_per_emp,
    x="REVENUE_PER_EMPLOYEE",
    y="NAME",
    orientation="h",
    title="Top 10 Companies by Revenue per Employee",
    labels={"REVENUE_PER_EMPLOYEE": "Revenue per Employee ($)", "NAME": "Company"},
    color="REVENUE_PER_EMPLOYEE",
    color_continuous_scale="Purples",
)
st.plotly_chart(fig_rev_per_emp)

# Interactive Map
st.subheader("Company Headquarters Map")
fig_map = px.scatter_mapbox(
    df,
    lat="LATITUDE",
    lon="LONGITUDE",
    hover_name="NAME",
    hover_data={"STATE": True, "REVENUES": True, "EMPLOYEES": True},
    color="REVENUES",
    size="REVENUES",
    color_continuous_scale="Plasma",
    zoom=3,
    title="Company Headquarters",
)
fig_map.update_layout(mapbox_style="carto-positron")
st.plotly_chart(fig_map)

# Interactive Leaderboard
st.subheader("Interactive Leaderboard")
st.dataframe(
    df[["RANK", "NAME", "STATE", "REVENUES", "EMPLOYEES", "PROFIT"]]
    .sort_values(by="RANK")
    .reset_index(drop=True)
)

# Additional Notes
st.info("Use the sidebar to filter companies by state, revenue, and employees for tailored insights.")

# Footer
st.markdown(
    """
    ---
    **Developed by: Joshua Dwinell**  
    **Course: CS230**
    """
)
