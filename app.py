import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Music Mood Classifier 🎵")

st.write("Enter the values for the following features:")

# Input fields for 6 features (replace names and ranges as per your data)
valence = st.number_input('Valence', min_value=0.0, max_value=1.0, value=0.5)
energy = st.number_input('Energy', min_value=0.0, max_value=1.0, value=0.5)
tempo = st.number_input('Tempo', min_value=0.0, max_value=250.0, value=120.0)
accousticness = st.number_input('Acousticness', min_value=0.0, max_value=1.0, value=0.5)
danceability = st.number_input('Danceability', min_value=0.0, max_value=1.0, value=0.5)

# Prepare features for prediction
features = np.array([[valence, energy, tempo, accousticness, danceability]])

if st.button('Predict Mood'):
    prediction = model.predict(features)
    st.success(f"The predicted music mood is: {prediction[0]}")
