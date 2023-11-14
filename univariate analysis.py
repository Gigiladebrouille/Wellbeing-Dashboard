"""
# Univariate Analysis Tab Script

This script is designed to handle the functionalities of the Univariate Analysis tab in the main dashboard.
It provides visualizations and statistics for individual variables in the dataset.

## How to Use:
1. Import this script into your main Streamlit dashboard script.
2. Call the `show_univariate_analysis_tab(data)` function and pass the DataFrame `data` as an argument.

"""

# Import Required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_univariate_analysis_tab(data):
    """
    Display the Univariate Analysis tab content on the Streamlit app.

    Parameters:
    - data (DataFrame): The dataset to analyze.

    Returns:
    None
    """
    st.title('Univariate Analysis of Variables')

    # Extract numerical and categorical columns
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = data.select_dtypes(include=['object']).columns

    # User selection for variable type
    variable_type = st.selectbox("Choose the type of variable for analysis", ["Numerical", "Categorical"])

    if variable_type == "Numerical":
        # User selection for numerical variable
        selected_var = st.selectbox("Choose a numerical variable", numeric_cols)

        # Display histogram
        st.subheader(f"Histogram of {selected_var}")
        fig, ax = plt.subplots()
        sns.histplot(data[selected_var], bins=30, ax=ax)
        st.pyplot(fig)

        # Display boxplot
        st.subheader(f"Boxplot of {selected_var}")
        fig, ax = plt.subplots()
        sns.boxplot(x=data[selected_var], ax=ax)
        st.pyplot(fig)

    elif variable_type == "Categorical":
        # User selection for categorical variable
        selected_var = st.selectbox("Choose a categorical variable", categorical_cols)

        # Display bar chart
        st.subheader(f"Bar Chart of {selected_var}")
        fig, ax = plt.subplots()
        sns.countplot(data=data, x=selected_var, ax=ax)
        st.pyplot(fig)

# Example usage in your main Streamlit script
# from univariate_analysis_tab_script import show_univariate_analysis_tab
# show_univariate_analysis_tab(data)