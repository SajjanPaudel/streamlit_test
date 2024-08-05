import streamlit as st

st.title('🎈Testing streamlit for data science')

with st.sidebar:
  st.write('**PARAMETERS TO CHANGE**')
with st.expander('DATA'):
  st.write('Hello world!')
