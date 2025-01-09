import streamlit as st
import pickle
import os

# Check if the model file exists
if os.path.exists("password_strength_model.pkl") and os.path.exists("vectorizer.pkl"):
    # Load the saved model and vectorizer
    with open("password_strength_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    with open("vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    # Define the prediction function
    def predict_strength(password):
        password_vec = vectorizer.transform([password])
        prediction = model.predict(password_vec)
        return prediction[0]

    # Streamlit app layout
    st.title('Password Strength Checker')

    password = st.text_input('Enter Password')

    if password:
        strength = predict_strength(password)
        st.write(f'Predicted Strength: {strength}')
else:
    st.error("Model or vectorizer file not found.")
