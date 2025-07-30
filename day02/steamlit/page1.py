import streamlit as st
import pandas as pd

st.markdown("# Page 1 ❄️")
st.sidebar.markdown("# Page 1 ❄️")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

with st.form("feedback_form"):
    st.header("Feedback form")

    # Creating columns to organize the form
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Please enter your name")
        rating = st.slider("Please rate this app", 0, 10, 5)
    with col2:
        dob = st.date_input("Please enter your date of birth")
        recommend = st.radio("Would you recommend this app to others?", ("Yes", "No"))

    submit_button = st.form_submit_button("Submit")

if submit_button is True:
    st.write(
        "**Name:**",
        name,
        "**Date of birth:**",
        dob,
        "**Rating:**",
        rating,
        "**Would recommend?:**",
        recommend,
    )