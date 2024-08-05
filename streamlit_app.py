import streamlit as st
import pandas as pd

st.title('🎈Testing streamlit for data science')
restaurant_data = pd.read_csv('https://raw.githubusercontent.com/suyogdahal/KhajaTime/master/KhajaTime.csv')
#get location of user
def get_user_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        
        location = {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "location": data.get("loc"),  # Latitude and Longitude
            "org": data.get("org")
        }
        
        return location
    except requests.RequestException as e:
        print(f"Error fetching location: {e}")
        return None

# Example usage
user_location = get_user_location()
if user_location:
  user_location_df = pd.DataFrame(user_location)
else:
    print("Could not fetch user location.")


with st.sidebar:
  st.write('**PARAMETERS TO CHANGE**')
with st.expander('DATA'):
  st.write('Hello world!')
  user_location
  restaurant_data
