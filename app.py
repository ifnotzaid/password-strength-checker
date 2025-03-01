import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open("password_strength_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Function to extract features from the password
def extract_features(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    entropy = -sum((password.count(c) / len(password)) * np.log2(password.count(c) / len(password)) for c in set(password))
    return [length, has_upper, has_number, has_special, entropy]

# Define the prediction function
def predict_strength(password):
    features = extract_features(password)  # Extract features
    prediction = model.predict([features])  # Make prediction
    return prediction[0]

# Streamlit app layout
st.title('Password Strength Checker')

password = st.text_input('Enter Password')

if password:
    # Check if password length is less than 8
    if len(password) < 8:
        st.markdown('<p style="color:red;">Weak</p>', unsafe_allow_html=True)
    else:
        strength = predict_strength(password)
        if strength == 0:
            st.markdown('<p style="color:red;">Weak</p>', unsafe_allow_html=True)
        elif strength == 1:
            st.markdown('<p style="color:yellow;">Good</p>', unsafe_allow_html=True)
        elif strength == 2:
            st.markdown('<p style="color:green;">Strong</p>', unsafe_allow_html=True)
