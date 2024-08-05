import streamlit as st
import pandas as pd
import requests 

st.title('🎈Testing streamlit for data science')
restaurant_data = pd.read_csv('https://raw.githubusercontent.com/suyogdahal/KhajaTime/master/KhajaTime.csv')

# Define a function to get the user's location using JavaScript
def get_user_location():
    location_js = """
    <script>
    function getLocation() {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const {latitude, longitude} = position.coords;
                const locationData = `${latitude},${longitude}`;
                const locationDiv = document.getElementById('location_data');
                locationDiv.innerText = locationData;
                locationDiv.dispatchEvent(new Event('location_available'));
            },
            (error) => {
                console.error(error);
                const locationDiv = document.getElementById('location_data');
                locationDiv.innerText = 'Error';
                locationDiv.dispatchEvent(new Event('location_available'));
            }
        );
    }
    getLocation();
    </script>
    <div id="location_data" style="display: none;"></div>
    """
    return location_js

# Add a header to the app
st.header('User Location')

# Display the JavaScript to fetch location
st.components.v1.html(get_user_location(), height=0)

# Placeholder for location data
if 'location' not in st.session_state:
    st.session_state['location'] = 'Fetching location...'

# Display the location
location = st.empty()
location.text(st.session_state['location'])

# JavaScript to get the location data from the hidden div and update session state
location_js = """
<script>
const locationDiv = document.getElementById('location_data');
locationDiv.addEventListener('location_available', function() {
    const locationData = locationDiv.innerText;
    if (window.parent) {
        window.parent.postMessage(locationData, '*');
    }
});
</script>
"""

# Add the JavaScript to the Streamlit app
st.components.v1.html(location_js, height=0)

# Listen for the location data message from the browser
location_data = st.experimental_get_query_params().get('location', [''])[0]
if location_data and location_data != 'Error':
    st.session_state['location'] = location_data
    location.text(f"Location: {location_data}")
else:
    st.session_state['location'] = 'Could not fetch location'
    location.text(st.session_state['location'])


with st.sidebar:
  st.write('**PARAMETERS TO CHANGE**')
with st.expander('DATA'):
  st.write('Hello world!')
  restaurant_data
