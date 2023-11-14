"""
# Logistic Regression Analysis Tab Script

This script is designed to handle the functionalities of the Logistic Regression Analysis tab in the main dashboard.
It provides a logistic regression model to predict employee attrition based on selected features.

## How to Use:
1. Import this script into your main Streamlit dashboard script.
2. Call the `show_logistic_regression_tab(data)` function and pass the DataFrame `data` as an argument.

"""

# Import Required Libraries
import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

def show_logistic_regression_tab(data):
    """
    Display the Logistic Regression Analysis tab content on the Streamlit app.

    Parameters:
    - data (DataFrame): The dataset to analyze.

    Returns:
    None
    """
    st.title('Logistic Regression Analysis')

    # Feature selection and data preparation
    selected_features = ['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company']
    X = data[selected_features]
    y = data['left']

    # Model training
    model = LogisticRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Display Confusion Matrix
    st.subheader('Confusion Matrix')
    cm = confusion_matrix(y, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    st.pyplot(fig)

    # Display Classification Report
    st.subheader('Classification Report')
    report = classification_report(y, y_pred)
    st.text(report)

    # Interpretation
    st.subheader('Interpretation')
    st.write("""
    The confusion matrix and classification report provide a detailed analysis of the model's performance.
    - Precision: The ratio of true positive predictions to the total predicted positives.
    - Recall: The ratio of true positive predictions to the total actual positives.
    - F1-Score: The weighted average of Precision and Recall.
    """)

# Example usage in your main Streamlit script
# from logistic_regression_tab_script import show_logistic_regression_tab
# show_logistic_regression_tab(data)