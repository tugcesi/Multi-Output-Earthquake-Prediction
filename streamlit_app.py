import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

st.title('Deprem Büyüklüğü ve Derinliği Tahmin Uygulaması')

st.sidebar.header('Parametreleri Giriniz')
latitude = st.sidebar.number_input("Enlem (Latitude)", value=38.5)
longitude = st.sidebar.number_input("Boylam (Longitude)", value=35.5)
year = st.sidebar.number_input("Yıl", value=2023, min_value=1900, max_value=2100)
month = st.sidebar.number_input("Ay", value=1, min_value=1, max_value=12)
day = st.sidebar.number_input("Gün", value=1, min_value=1, max_value=31)
hour = st.sidebar.number_input("Saat", value=0, min_value=0, max_value=23)
minute = st.sidebar.number_input("Dakika", value=0, min_value=0, max_value=59)

feature_order = ['Latitude', 'Longitude', 'Year', 'Month', 'Day', 'Hour', 'Minute']
user_input = np.array([[latitude, longitude, year, month, day, hour, minute]])

def load_model():
    try:
        model = joblib.load('earthquake_pred.joblib')
        return model, None
    except Exception:
        pass
    try:
        with open('earthquake_pred.pkl', 'rb') as f:
            obj = pickle.load(f)
            return obj['model'], obj.get('features', None)
    except Exception:
        pass
    return None, None

model, features = load_model()

if model is None:
    st.error('Model dosyası bulunamadı! earthquake_pred.joblib veya earthquake_pred.pkl dosyasını ana dizine koyunuz.')
else:
    if st.button('Tahmin Et'):
        prediction = model.predict(user_input)
        st.success(f"Tahmini Büyüklük: {prediction[0][0]:.2f}")
        st.info(f"Tahmini Derinlik: {prediction[0][1]:.2f}")