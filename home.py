import streamlit as st

st.title("Welcome to My Streamlit App")
st.write("This is the home page. Click the button below to navigate to the application page.")

if st.button("Go to App"):
    st.switch_page("pages/APP.py")
