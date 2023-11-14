"""
# Contingency Analysis Tab Script

This script is designed to handle the functionalities of the Contingency Analysis tab in the main dashboard.
It provides a contingency table for selected categorical variables in the dataset.

## How to Use:
1. Import this script into your main Streamlit dashboard script.
2. Call the `show_contingency_analysis_tab(data)` function and pass the DataFrame `data` as an argument.

"""

# Import Required Libraries
import streamlit as st
import pandas as pd

def show_contingency_analysis_tab(data):
    """
    Display the Contingency Analysis tab content on the Streamlit app.

    Parameters:
    - data (DataFrame): The dataset to analyze.

    Returns:
    None
    """
    st.title('Contingency Analysis of Categorical Variables')

    # Extract categorical columns
    categorical_cols = data.select_dtypes(include=['object', 'bool']).columns

    # Display selection options for variables
    var1 = st.selectbox("Choose the first variable", categorical_cols)
    var2 = st.selectbox("Choose the second variable", categorical_cols)

    # Calculate the contingency table
    table = pd.crosstab(data[var1], data[var2], margins=True)

    st.subheader('Contingency Table')
    # Display the contingency table
    st.write(table)

# Example usage in your main Streamlit script
# from contingency_analysis_tab_script import show_contingency_analysis_tab
# show_contingency_analysis_tab(data)