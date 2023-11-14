"""
# Statistics Tab Script

This script is designed to handle the functionalities of the Statistics tab in the main dashboard.
It provides descriptive statistics for numerical variables in the dataset.

## How to Use:
1. Import this script into your main Streamlit dashboard script.
2. Call the `show_statistics_tab(data)` function and pass the DataFrame `data` as an argument.

"""

# Import Required Libraries
import streamlit as st
import pandas as pd
import numpy as np

def show_statistics_tab(data):
    """
    Display the Statistics tab content on the Streamlit app.

    Parameters:
    - data (DataFrame): The dataset to analyze.

    Returns:
    None
    """
    st.title('Descriptive Statistics for Numerical Variables')

    # Extract numerical columns
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns

    # Calculate descriptive statistics
    stats = data[numeric_cols].describe()

    # Display the statistics table
    st.write("Overview of statistics:")
    st.dataframe(stats)

    # Highlight key statistics with widgets
    st.write("Key Statistics:")

    col1, col2, col3 = st.columns(3)

    for col in numeric_cols:
        mean_val = data[col].mean()
        median_val = data[col].median()
        std_val = data[col].std()

        # Identify outliers
        outlier_condition = np.abs(data[col] - mean_val) > 2 * std_val
        num_outliers = np.sum(outlier_condition)

        # Use color code for outliers
        outlier_color = 'red' if num_outliers > 0 else 'green'

        with col1:
            st.metric(label=f"Mean of {col}", value=f"{mean_val:.2f}")
        with col2:
            st.metric(label=f"Median of {col}", value=f"{median_val:.2f}")
        with col3:
            st.metric(label=f"Standard Deviation of {col}", value=f"{std_val:.2f}")

        st.write(f"Number of outliers for {col}: ", num_outliers, f"🚨" if num_outliers > 0 else "✅")

    # Display percentiles
    st.write("Percentiles:")
    for col in numeric_cols:
        percentiles = np.percentile(data[col], [25, 50, 75])
        st.write(f"For {col}, the 25th, 50th, and 75th percentiles are {percentiles}")

# Example usage in your main Streamlit script
# from statistics_tab_script import show_statistics_tab
# show_statistics_tab(data)
