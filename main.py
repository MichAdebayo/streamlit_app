import streamlit as st
from app_pages.quiz import quiz_page  # Import quiz page function
from app_pages.questionnaire import configure_questionnaire  # Import questionnaire page function

# Sidebar for page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Configure your questionnaire", "Start quiz"])

# Display the selected page
if page == "Configure your questionnaire":
    configure_questionnaire()  # Call the questionnaire function
elif page == "Start quiz":
    quiz_page()  # Call the quiz page function
    



