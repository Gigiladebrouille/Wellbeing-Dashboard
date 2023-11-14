"""
# Correlation Analysis Tab Script

This script is designed to handle the functionalities of the Correlation Analysis tab in the main dashboard.
It provides a heatmap and statistics for the correlation between numerical variables in the dataset.

## How to Use:
1. Import this script into your main Streamlit dashboard script.
2. Call the `show_correlation_analysis_tab(data)` function and pass the DataFrame `data` as an argument.

"""

# Import Required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_correlation_analysis_tab(data):
    """
    Display the Correlation Analysis tab content on the Streamlit app.

    Parameters:
    - data (DataFrame): The dataset to analyze.

    Returns:
    None
    """
    st.title('Correlation Analysis of Numerical Variables')

    # Extract numerical columns
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns

    # Calculate the correlation matrix
    corr_matrix = data[numeric_cols].corr()

    # Display correlation matrix
    st.subheader('Correlation Matrix')
    st.write(corr_matrix.round(4))

    # Display heatmap
    st.subheader('Correlation Heatmap')
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Example usage in your main Streamlit script
# from correlation_analysis_tab_script import show_correlation_analysis_tab
# show_correlation_analysis_tab(data)
