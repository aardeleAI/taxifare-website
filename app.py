import streamlit as st
import requests
import pandas as pd
from datetime import datetime


'''
# BestCabFare Price Estimator
'''

st.markdown('''
This is the first minimalist alternative to Uber
''')

'''
## Please enter your fare details
'''
st.markdown('''
⚠️🚧 Due to website maintenance, only "**A LA MANO**" entered geographic coordinates for your departure and arrival locations will be accepted 🚧⚠️
''')

pickup_date = st.date_input("Pickup date")
pickup_time = st.time_input("Pickup time")
pickup_longitude = st.number_input("Pickup longitude")
pickup_latitude = st.number_input("Pickup latitude")
dropoff_longitude = st.number_input("Dropoff longitude")
dropoff_latitude = st.number_input("Dropoff latitude")
passenger_count = st.number_input("Passenger count", min_value=1, max_value=8)

pickup_datetime = datetime.combine(pickup_date, pickup_time)

params = {"pickup_datetime": pickup_datetime,
          "pickup_longitude": pickup_longitude,
          "pickup_latitude": pickup_latitude,
          "dropoff_longitude": dropoff_longitude,
          "dropoff_latitude": dropoff_latitude,
          "passenger_count": passenger_count} # Création du dictionnaire des paramètres

manhattan_latitude = 40.7580
manhattan_longitude = -73.9855

df = pd.DataFrame({
    "lat": [manhattan_latitude],
    "lon": [manhattan_longitude]
})

st.map(df)

url = 'https://taxifare.lewagon.ai/predict'

if st.button("Predict fare price"):
    response = requests.get(url, params=params) # Créer la requête à mon API
    prediction = response.json()
    st.write(f"Estimated fare price: $ {prediction['fare']: .2f}")
