# Streamlit Dashboard Project for Employee Well-being

## Introduction

This project is a dashboard application developed with Streamlit to analyze employee well-being. It is primarily a personal project aimed at exploring the capabilities of Streamlit and showcasing my skills in Python and as a Site Reliability Engineer (SRE).

The context of employee well-being is used here as an example to demonstrate how Streamlit and SRE principles can be applied in the field of human resources to improve system reliability and availability.

## Features

- **Univariate, bivariate, and multivariate analysis**
- **Statistical tests** such as ANOVA, Chi-square, etc.
- **Correlation matrix**
- **Logistic regression** for prediction
- And much more...

## Installation and Execution

### Prerequisites

- Python 3.8 or higher
- Docker (optional)

### Installation

1. **Clone this GitHub repository.**
2. **Navigate to the project directory.**
3. **Install dependencies** using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

### Execution

- **Without Docker**:

    ```bash
    streamlit run Dashboard.py
    ```

- **With Docker**:

    ```bash
    docker build -t my_dashboard .
    docker run -p 8501:8501 my_dashboard
    ```

## Contribution

This project is open to contributions. Feel free to open an issue or submit a pull request.
