
# ! Model
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

iris = load_iris()
X = iris.data
y = iris.target

model = LinearRegression()
model.fit(X, y)



# ! FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
async def predict_species(features: IrisFeatures):
    X = [[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]]
    y_pred = model.predict(X)
    return {"species": int(y_pred[0])}

# ! Streamlit
import requests
import streamlit as st

# API endpoint
url = "http://localhost:8000/predict"

# kullanıcı arayüzü
st.title("Iris Çiçeği Türü Tahmini")

sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Tahmin Et"):
    response = requests.post(url, json={"sepal_length": sepal_length, "sepal_width": sepal_width, "petal_length": petal_length, "petal_width": petal_width})
    species = response.json()["species"]
    st.write(f"Bu çiçek {iris.target_names[species]} türüdür.")
