# iris-prediction-fastapi-streamlit (Building a Linear Regression Model on the Iris Dataset and Creating a Web Application)

This project builds a linear regression model on the Iris dataset and creates a web application that can make flower type predictions using the model.

Requirements
To run this project, you need to have the following software installed on your computer:

Python 3.7 or higher
pip
Installation
Clone this repository to your computer.

Open a terminal and navigate to the directory where you cloned the repository.

Use the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```
## Usage
* Open a terminal and navigate to the directory where you cloned the repository.

* Use the following command to start the FastAPI application:
```bash
uvicorn main:app --reload
```
* Use the following command to start the Streamlit application:
```bash
streamlit run app.py
```
* Open http://localhost:8501 in your web browser to access the web application.

* Use the form on the page to make a flower type prediction based on the feature values you select.
