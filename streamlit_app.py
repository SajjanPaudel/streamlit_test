import streamlit as st
import pandas as pd
import requests 

st.title('🎈Testing streamlit for data science')
restaurant_data = pd.read_csv('https://raw.githubusercontent.com/suyogdahal/KhajaTime/master/KhajaTime.csv')


# Define a function to get the user's location
def get_user_location():
    location_js = """
    <script>
    function getLocation() {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const {latitude, longitude} = position.coords;
                document.getElementById('location_data').innerText = `${latitude},${longitude}`;
            },
            (error) => {
                console.error(error);
                document.getElementById('location_data').innerText = 'Error';
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
location = st.empty()

# Display the location
location.text('Fetching location...')

# JavaScript to get the location data from the browser
location_data = st.components.v1.html(
    """
    <script>
    const getLocation = () => {
        return new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const {latitude, longitude} = position.coords;
                    resolve(`${latitude},${longitude}`);
                },
                (error) => {
                    reject('Error');
                }
            );
        });
    };

    getLocation().then((data) => {
        document.getElementById('location_data').innerText = data;
    }).catch((error) => {
        document.getElementById('location_data').innerText = error;
    });
    </script>
    <div id="location_data" style="display: none;"></div>
    """,
    height=0
)

# Get the location from the hidden div
if location_data:
    st.write('Location:', location_data)
else:
    st.write('Could not fetch location')


with st.sidebar:
  st.write('**PARAMETERS TO CHANGE**')
with st.expander('DATA'):
  st.write('Hello world!')
  restaurant_data
