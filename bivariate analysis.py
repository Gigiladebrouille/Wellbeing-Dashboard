"""
# Bivariate Analysis Tab Script

This script is designed to handle the functionalities of the Bivariate Analysis tab in the main dashboard.
It provides visualizations and statistics for the relationship between two variables in the dataset.

## How to Use:
1. Import this script into your main Streamlit dashboard script.
2. Call the `show_bivariate_analysis_tab(data)` function and pass the DataFrame `data` as an argument.

"""

# Import Required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

def show_bivariate_analysis_tab(data):
    """
    Display the Bivariate Analysis tab content on the Streamlit app.

    Parameters:
    - data (DataFrame): The dataset to analyze.

    Returns:
    None
    """
    st.title('Bivariate Analysis of Variables')

    # Extract numerical and categorical columns
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = data.select_dtypes(include=['object']).columns

    # User selection for variable type
    var1 = st.selectbox("Choose the first variable", numeric_cols)
    var2 = st.selectbox("Choose the second variable", numeric_cols)

    # Display scatter plot
    st.subheader(f"Scatter Plot between {var1} and {var2}")
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=var1, y=var2, ax=ax)
    st.pyplot(fig)

    # Display correlation coefficient
    corr, _ = pearsonr(data[var1], data[var2])
    st.write(f"The correlation coefficient between {var1} and {var2} is {corr:.2f}")

# Example usage in your main Streamlit script
# from bivariate_analysis_tab_script import show_bivariate_analysis_tab
# show_bivariate_analysis_tab(data)