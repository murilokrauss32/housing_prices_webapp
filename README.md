# House Pricing Prediction Web App

This is a Flask-based web application for predicting house prices using machine learning models. The application allows users to input various features of a house and choose between two models—Random Forest and LightGBM—to estimate the house price.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributors](#contributors)

## Features

- User input for house features
- Two machine learning models (Random Forest and LightGBM) for prediction
- Validation of input values
- Deployment-ready for PythonAnywhere

## Requirements

- Python 3.8+
- Flask==3.0.3
- numpy==1.26.4
- pandas==2.2.2
- scikit-learn==1.5.0
- lightgbm==4.3.0

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/YOUR_USERNAME/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure the project structure is as follows:

    ```
    housing_prices_webapp/
    |-- app.py
    |-- models/
    |   |-- random_forest_tuned_important.pkl
    |   |-- lightgbm_tuned_important.pkl
    |-- static/
    |   |-- style.css
    |-- templates/
    |   |-- index.html
    |-- requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Input the house features and select a model to predict the house price.

## Deployment

### Deploying to PythonAnywhere

1. Create an account on [PythonAnywhere](https://www.pythonanywhere.com/) and log in.
2. Upload your project files to PythonAnywhere.
3. Create a virtual environment on PythonAnywhere and install the requirements.
4. Configure the web app settings on PythonAnywhere, ensuring the WSGI configuration points to your Flask app.
5. Reload the web app and test the deployment.

## Contributors

- Murilo Krauss

