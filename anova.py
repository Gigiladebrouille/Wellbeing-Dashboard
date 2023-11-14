"""
# ANOVA Analysis Tab Script

This script is designed to handle the functionalities of the ANOVA Analysis tab in the main dashboard.
It provides an ANOVA table for selected numerical variables in the dataset.

## How to Use:
1. Import this script into your main Streamlit dashboard script.
2. Call the `show_anova_analysis_tab(data)` function and pass the DataFrame `data` as an argument.

"""

# Import Required Libraries
import streamlit as st
import pandas as pd
import scipy.stats as stats

def show_anova_analysis_tab(data):
    """
    Display the ANOVA Analysis tab content on the Streamlit app.

    Parameters:
    - data (DataFrame): The dataset to analyze.

    Returns:
    None
    """
    st.title('ANOVA Analysis of Numerical Variables')

    # Extract numerical columns
    numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns

    # Display selection options for variables
    var1 = st.selectbox("Choose the first variable", numerical_cols)
    var2 = st.selectbox("Choose the second variable", numerical_cols)

    # Perform ANOVA
    f_val, p_val = stats.f_oneway(data[var1], data[var2])

    st.subheader('ANOVA Results')
    st.write(f"F-value: {f_val}")
    st.write(f"P-value: {p_val}")

    # Interpretation
    if p_val < 0.05:
        st.write("The variables have a statistically significant difference.")
    else:
        st.write("The variables do not have a statistically significant difference.")

# Example usage in your main Streamlit script
# from anova_analysis_tab_script import show_anova_analysis_tab
# show_anova_analysis_tab(data)