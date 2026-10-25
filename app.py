import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('model.sav')

# Set up the title and description of the app
st.title("Advertising Sales Predictor")
st.write("This app predicts sales based on TV, Radio, and Newspaper advertising budgets.")

# Create input fields for the user
tv = st.number_input("TV Budget ($)", min_value=0.0, step=1.0, value=100.0)
radio = st.number_input("Radio Budget ($)", min_value=0.0, step=1.0, value=20.0)
newspaper = st.number_input("Newspaper Budget ($)", min_value=0.0, step=1.0, value=15.0)

# Prediction trigger
if st.button("Predict Sales"):
    # Prepare the input features as a DataFrame to keep feature names
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display the result
    st.success(f"Estimated Sales: {prediction:.2f} units")
