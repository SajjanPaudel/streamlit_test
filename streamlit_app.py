import streamlit as st
import pandas as pd
import requests 
from streamlit_javascript import st_javascript

st.title('🎈Testing streamlit for data science')
restaurant_data = pd.read_csv('https://raw.githubusercontent.com/suyogdahal/KhajaTime/master/KhajaTime.csv')


# Define the HTML and JavaScript code
html_code = """
<!DOCTYPE html>
<html>
<body>

<h2>User Location</h2>
<p id="demo">Fetching location...</p>

<script>
const x = document.getElementById("demo");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition, showError);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;

  // Send data to Streamlit
  const streamlitMessage = `${position.coords.latitude},${position.coords.longitude}`;
  window.parent.postMessage(streamlitMessage, "*");
}

function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      x.innerHTML = "User denied the request for Geolocation.";
      break;
    case error.POSITION_UNAVAILABLE:
      x.innerHTML = "Location information is unavailable.";
      break;
    case error.TIMEOUT:
      x.innerHTML = "The request to get user location timed out.";
      break;
    case error.UNKNOWN_ERROR:
      x.innerHTML = "An unknown error occurred.";
      break;
  }
}

// Automatically request location on page load
window.onload = getLocation;
</script>

</body>
</html>
"""

# Embed the HTML and JavaScript code in Streamlit
st.components.v1.html(html_code, height=300)

# Function to capture location data sent from JavaScript
def get_location():
    location_data = st.experimental_get_query_params().get('location', [''])[0]
    if location_data:
        return location_data
    return None

# Display the location
location = get_location()
if location:
    st.write(f"Location: {location}")
else:
    st.write("Fetching location...")

with st.sidebar:
  st.write('**PARAMETERS TO CHANGE**')
with st.expander('DATA'):
  st.write('Hello world!')
  restaurant_data
