import streamlit as st
import pickle
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Iris Species Predictor",
    page_icon="🌸",
    layout="centered"
)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title("🌸 Iris Species Predictor")
st.markdown("### Predict the species of an Iris flower based on its measurements")

st.write("Enter the measurements of the iris flower below to predict its species.")

# Input fields
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Prediction
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    species = ['Setosa', 'Versicolor', 'Virginica'][prediction[0]]
    st.write(f"Predicted Species: {species}")