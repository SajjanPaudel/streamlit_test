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
<p>Click the button to get your coordinates:</p>

<button onclick="getLocation()">Try It</button>

<p id="demo"></p>

<script>
const x = document.getElementById("demo");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
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
    st.write("Click the button above to fetch your location.")


with st.sidebar:
  st.write('**PARAMETERS TO CHANGE**')
with st.expander('DATA'):
  st.write('Hello world!')
  restaurant_data
