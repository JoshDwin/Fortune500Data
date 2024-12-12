{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JoshDwin/Fortune500Data/blob/main/Final_Project.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BL5qh9fUYOVB",
        "outputId": "4e2cc1f1-8472-4fb7-fd84-15221dfc9c7a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-12-12 22:02:23.716 No runtime found, using MemoryCacheStorageManager\n",
            "2024-12-12 22:02:23.736 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.738 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.742 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.744 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.748 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.750 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.753 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.756 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.762 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.765 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.770 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.782 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.785 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.788 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.791 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.795 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.827 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.830 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.832 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.835 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.837 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.839 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.841 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.844 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.846 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.851 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.852 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.854 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.855 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.859 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.864 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.868 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.871 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.873 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.877 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.879 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:23.883 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.050 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.055 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.060 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.063 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.065 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.151 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.154 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.162 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.167 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.169 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.254 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.256 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.260 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.262 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.265 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.267 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.339 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.342 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.345 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.347 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.350 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.354 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.445 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.451 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.453 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.455 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.461 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.471 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.473 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.477 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.480 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.484 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-12 22:02:24.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ],
      "source": [
        "\"\"\"\n",
        "Name: Joshua Dwinell\n",
        "CS230: 2\n",
        "Data: Fortune 500 Data\n",
        "URL: Link to your web application on Streamlit Cloud (if posted)\n",
        "\n",
        "Description: This program creates a website that shows many important information from the Fortune 500 data.\n",
        "It shows top 10 graphs for many important pieces of data such as revenue, revenue per employee, employee count, and more.\n",
        "It also includes a map and sliders and dropdowns to filter the data by state, revenue, and employee count.\n",
        "\n",
        "\"\"\"\n",
        "# Used a lot og google, youtube, and just research to figure out how to do a lot of things in this code\n",
        "\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "# Used google to find this import function to use\n",
        "import plotly.express as px\n",
        "\n",
        "# Load Data\n",
        "@st.cache_data\n",
        "def load_data():\n",
        "    file_path = \"fortune_500_hq.xlsx\"\n",
        "    try:\n",
        "        df = pd.read_excel(file_path)\n",
        "    except FileNotFoundError:\n",
        "        st.error(\"The data file was not found. Please make sure 'fortune_500_hq.xlsx' is in the correct location.\")\n",
        "        return pd.DataFrame()\n",
        "    except Exception as e:\n",
        "        st.error(f\"An error occurred while loading the data: {e}\")\n",
        "        return pd.DataFrame()\n",
        "    return df\n",
        "\n",
        "df = load_data()\n",
        "\n",
        "if df.empty:\n",
        "    st.stop()\n",
        "\n",
        "# Handle Missing Data\n",
        "df.fillna({\"REVENUES\": 0, \"EMPLOYEES\": 1, \"PROFIT\": 0, \"LATITUDE\": 0, \"LONGITUDE\": 0}, inplace=True)\n",
        "df.dropna(subset=[\"NAME\", \"STATE\"], inplace=True)\n",
        "\n",
        "# Preprocess Data\n",
        "df[\"REVENUE_PER_EMPLOYEE\"] = df[\"REVENUES\"] / df[\"EMPLOYEES\"]\n",
        "df[\"STATE\"] = df[\"STATE\"].str.upper()\n",
        "\n",
        "# Sidebar\n",
        "st.sidebar.title(\"Filter Options\")\n",
        "state_filter = st.sidebar.multiselect(\"Filter by States:\", options=sorted(df[\"STATE\"].dropna().unique()), default=None)\n",
        "if state_filter:\n",
        "    df = df[df[\"STATE\"].isin(state_filter)]\n",
        "\n",
        "revenue_range = st.sidebar.slider(\"Filter by Revenue ($M):\", min_value=0, max_value=int(df[\"REVENUES\"].max()), value=(0, int(df[\"REVENUES\"].max())))\n",
        "df = df[(df[\"REVENUES\"] >= revenue_range[0]) & (df[\"REVENUES\"] <= revenue_range[1])]\n",
        "\n",
        "employee_range = st.sidebar.slider(\"Filter by Employee Count:\", min_value=0, max_value=int(df[\"EMPLOYEES\"].max()), value=(0, int(df[\"EMPLOYEES\"].max())))\n",
        "df = df[(df[\"EMPLOYEES\"] >= employee_range[0]) & (df[\"EMPLOYEES\"] <= employee_range[1])]\n",
        "\n",
        "# Add Download Button\n",
        "# Googled how to do this\n",
        "st.sidebar.download_button(\n",
        "    label=\"Download Filtered Data as CSV\",\n",
        "    data=df.to_csv(index=False),\n",
        "    file_name=\"filtered_fortune_500_data.csv\",\n",
        "    mime=\"text/csv\",\n",
        ")\n",
        "\n",
        "# Main Page Title\n",
        "# Used chat GPT to help with this\n",
        "st.markdown(\n",
        "    \"\"\"\n",
        "    <style>\n",
        "        body {\n",
        "            background-color: #f4f4f9;\n",
        "        }\n",
        "        .main {\n",
        "            background-color: #ffffff;\n",
        "            border-radius: 10px;\n",
        "            padding: 10px;\n",
        "            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);\n",
        "        }\n",
        "        .title {\n",
        "            text-align: center;\n",
        "            font-size: 36px;\n",
        "            font-family: 'Arial', sans-serif;\n",
        "            color: #2e77d0;\n",
        "            margin-bottom: 20px;\n",
        "        }\n",
        "    </style>\n",
        "    \"\"\",\n",
        "    unsafe_allow_html=True,\n",
        ")\n",
        "\n",
        "st.markdown('<div class=\"title\">Fortune 500 Insights</div>', unsafe_allow_html=True)\n",
        "st.write(\"Explore interactive visualizations and detailed insights from Fortune 500 companies.\")\n",
        "\n",
        "# Key Metrics\n",
        "total_revenue = df[\"REVENUES\"].sum()\n",
        "total_employees = df[\"EMPLOYEES\"].sum()\n",
        "avg_revenue_per_company = df[\"REVENUES\"].mean()\n",
        "top_company = df.loc[df[\"REVENUES\"].idxmax(), \"NAME\"]\n",
        "\n",
        "st.subheader(\"Key Metrics\")\n",
        "\n",
        "# Used Chat GPT to help with this\n",
        "st.markdown(\n",
        "    f\"\"\"\n",
        "    <div style=\"display: flex; justify-content: space-between; text-align: center;\">\n",
        "        <div><b>Total Revenue ($M):</b> {total_revenue:,.2f}</div>\n",
        "        <div><b>Total Employees:</b> {total_employees:,}</div>\n",
        "        <div><b>Average Revenue per Company ($M):</b> {avg_revenue_per_company:,.2f}</div>\n",
        "        <div><b>Top Revenue Company:</b> {top_company}</div>\n",
        "    </div>\n",
        "    \"\"\",\n",
        "    unsafe_allow_html=True,\n",
        ")\n",
        "\n",
        "# Graphs Section\n",
        "st.header(\"Data Visualizations\")\n",
        "\n",
        "# Top 10 Companies by Revenue\n",
        "st.subheader(\"Top 10 Companies by Revenue\")\n",
        "top_revenue = df.nlargest(10, \"REVENUES\")\n",
        "fig_revenue = px.bar(\n",
        "    top_revenue,\n",
        "    x=\"REVENUES\",\n",
        "    y=\"NAME\",\n",
        "    orientation=\"h\",\n",
        "    title=\"Top 10 Companies by Revenue\",\n",
        "    labels={\"REVENUES\": \"Revenue ($B)\", \"NAME\": \"Company\"},\n",
        "    color=\"REVENUES\",\n",
        "    color_continuous_scale=\"Blues\",\n",
        ")\n",
        "st.plotly_chart(fig_revenue)\n",
        "\n",
        "# Top 10 Companies by Employees\n",
        "st.subheader(\"Top 10 Companies by Employees\")\n",
        "top_employees = df.nlargest(10, \"EMPLOYEES\")\n",
        "fig_employees = px.bar(\n",
        "    top_employees,\n",
        "    x=\"EMPLOYEES\",\n",
        "    y=\"NAME\",\n",
        "    orientation=\"h\",\n",
        "    title=\"Top 10 Companies by Employees\",\n",
        "    labels={\"EMPLOYEES\": \"Number of Employees\", \"NAME\": \"Company\"},\n",
        "    color=\"EMPLOYEES\",\n",
        "    color_continuous_scale=\"Greens\",\n",
        ")\n",
        "st.plotly_chart(fig_employees)\n",
        "\n",
        "# Top States by Company Count\n",
        "st.subheader(\"Top States by Company Count\")\n",
        "state_counts = df[\"STATE\"].value_counts().nlargest(10)\n",
        "fig_states = px.bar(\n",
        "    state_counts,\n",
        "    x=state_counts.values,\n",
        "    y=state_counts.index,\n",
        "    orientation=\"h\",\n",
        "    title=\"Top 10 States by Company Count\",\n",
        "    labels={\"y\": \"State\", \"x\": \"Company Count\"},\n",
        "    color=state_counts.values,\n",
        "    color_continuous_scale=\"Viridis\",\n",
        ")\n",
        "st.plotly_chart(fig_states)\n",
        "\n",
        "# Revenue per Employee\n",
        "st.subheader(\"Top 10 Companies by Revenue per Employee\")\n",
        "top_rev_per_emp = df.nlargest(10, \"REVENUE_PER_EMPLOYEE\")\n",
        "fig_rev_per_emp = px.bar(\n",
        "    top_rev_per_emp,\n",
        "    x=\"REVENUE_PER_EMPLOYEE\",\n",
        "    y=\"NAME\",\n",
        "    orientation=\"h\",\n",
        "    title=\"Top 10 Companies by Revenue per Employee\",\n",
        "    labels={\"REVENUE_PER_EMPLOYEE\": \"Revenue per Employee ($)\", \"NAME\": \"Company\"},\n",
        "    color=\"REVENUE_PER_EMPLOYEE\",\n",
        "    color_continuous_scale=\"Purples\",\n",
        ")\n",
        "st.plotly_chart(fig_rev_per_emp)\n",
        "\n",
        "# Interactive Map\n",
        "st.subheader(\"Company Headquarters Map\")\n",
        "fig_map = px.scatter_mapbox(\n",
        "    df,\n",
        "    lat=\"LATITUDE\",\n",
        "    lon=\"LONGITUDE\",\n",
        "    hover_name=\"NAME\",\n",
        "    hover_data={\"STATE\": True, \"REVENUES\": True, \"EMPLOYEES\": True},\n",
        "    color=\"REVENUES\",\n",
        "    size=\"REVENUES\",\n",
        "    color_continuous_scale=\"Plasma\",\n",
        "    zoom=3,\n",
        "    title=\"Company Headquarters\",\n",
        ")\n",
        "fig_map.update_layout(mapbox_style=\"carto-positron\")\n",
        "st.plotly_chart(fig_map)\n",
        "\n",
        "# Interactive Leaderboard\n",
        "st.subheader(\"Interactive Leaderboard\")\n",
        "st.dataframe(\n",
        "    df[[\"RANK\", \"NAME\", \"STATE\", \"REVENUES\", \"EMPLOYEES\", \"PROFIT\"]]\n",
        "    .sort_values(by=\"RANK\")\n",
        "    .reset_index(drop=True)\n",
        ")\n",
        "\n",
        "# Additional Notes\n",
        "st.info(\"Use the sidebar to filter companies by state, revenue, and employees for tailored insights.\")\n",
        "\n",
        "# Footer\n",
        "st.markdown(\n",
        "    \"\"\"\n",
        "    ---\n",
        "    **Developed by: Joshua Dwinell**\n",
        "    **Course: CS230**\n",
        "    \"\"\"\n",
        ")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "fgg6UGtWsyUb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2149bcb8-a73f-4dac-c7e3-e8369e4f4a31"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m23.4/23.4 MB\u001b[0m \u001b[31m60.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m72.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m4.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ],
      "source": [
        "! pip install streamlit -q"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wsmMHZ65szMB"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n96BxhkXe5m1",
        "outputId": "5357e7f2-2cf6-42ec-bf3b-3b97d39eefd5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "34.82.176.44\n"
          ]
        }
      ],
      "source": [
        "!wget -q -O - ipv4.icanhazip.com"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tRGT4_cRfBRy",
        "outputId": "a4caf3fa-4689-47ff-dab4-94f2b366439d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eIPE39x9fIrz",
        "outputId": "1e108040-458a-43b8-e243-a881c49ab181"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.74.41.231:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n"
          ]
        }
      ],
      "source": [
        "!streamlit run app.py &"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tgGshLh5fWai",
        "outputId": "3cabc81b-20f1-4dbb-ba71-7fe686fb8a30"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.82.176.44:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0Kyour url is: https://salty-spiders-prove.loca.lt\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ],
      "source": [
        "!streamlit run app.py & npx localtunnel --port 8501"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP6tkLKdjsjHb62giOIay6y",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}