## Installation and Execution

### Prerequisites

- Python 3.8 or higher
- Docker (optional)
- Virtual Environment (recommended)

### Installation

1. **Clone this GitHub repository.**
2. **Navigate to the project directory.**
3. **Create a virtual environment (Optional but recommended):**

    ```bash
    python -m venv myenv
    ```

4. **Activate the virtual environment:**

    - **On Windows:**

        ```bash
        .\myenv\Scripts\Activate
        ```

    - **On macOS and Linux:**

        ```bash
        source myenv/bin/activate
        ```

5. **Install the dependencies** using the `requirements.txt` file:

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

This project is open for contributions. Feel free to open an issue or submit a pull request.
