import streamlit as st
import pandas as pd
import requests 
from streamlit_javascript import st_javascript

st.title('🎈Testing streamlit for data science')
restaurant_data = pd.read_csv('https://raw.githubusercontent.com/suyogdahal/KhajaTime/master/KhajaTime.csv')

# Add a header to the app
st.header('User Location')

# Define a JavaScript function to get the user's location
get_location_js = """
navigator.geolocation.getCurrentPosition(
    (position) => {
        const { latitude, longitude } = position.coords;
        const locationData = `${latitude},${longitude}`;
        window.location = `?location=${locationData}`;
    },
    (error) => {
        console.error(error);
        window.location = `?location=Error`;
    }
);
"""

# Use st_javascript to execute the JavaScript code
st_javascript(get_location_js)

# Read the location from the query parameters
location_data = st.experimental_get_query_params().get('location', [''])[0]

# Display the location
if location_data and location_data != 'Error':
    st.write(f"Location: {location_data}")
else:
    st.write("Could not fetch location")


with st.sidebar:
  st.write('**PARAMETERS TO CHANGE**')
with st.expander('DATA'):
  st.write('Hello world!')
  restaurant_data
