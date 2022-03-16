import streamlit as st
import settings
def app():
    st.title("Project- Data Management and Visualization")
    st.header("Welcome to the Crash/Fatalities Dashboard!")
    st.write("sneak peek of data")
    st.write(settings.get_data().astype(str).head())