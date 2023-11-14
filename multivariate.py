"""
# Multivariate Analysis Tab Script

This script is designed to handle the functionalities of the Multivariate Analysis tab in the main dashboard.
It provides a correlation matrix and heatmap for the selected numerical variables in the dataset.

## How to Use:
1. Import this script into your main Streamlit dashboard script.
2. Call the `show_multivariate_analysis_tab(data)` function and pass the DataFrame `data` as an argument.

"""

# Import Required Libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def show_multivariate_analysis_tab(data):
    """
    Display the Multivariate Analysis tab content on the Streamlit app.

    Parameters:
    - data (DataFrame): The dataset to analyze.

    Returns:
    None
    """
    st.title('Multivariate Analysis of Numerical Variables')

    # Extract numerical columns
    numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns

    # Calculate the correlation matrix
    corr_matrix = data[numerical_cols].corr()

    st.subheader('Correlation Matrix')
    st.write(corr_matrix.round(4))

    st.subheader('Correlation Heatmap')
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Interpretation
    st.subheader('Interpretation')
    st.write("""
    A correlation value close to 1 implies a strong positive correlation: as one variable increases, the second variable tends to also increase.
    A correlation value close to -1 implies a strong negative correlation: as one variable increases, the second variable tends to decrease.
    A value close to 0 implies no correlation: changes in one variable do not predict changes in the second variable.
    """)

# Example usage in your main Streamlit script
# from multivariate_analysis_tab_script import show_multivariate_analysis_tab
# show_multivariate_analysis_tab(data)