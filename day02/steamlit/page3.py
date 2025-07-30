import streamlit as st
import datetime

def click_button():
    name = st.text_input('Name')
    st.success(f'Welcome {name}')


st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
st.button('Click me', on_click=click_button)
st.date_input('시작일과 종료일',value=[datetime.date(2019,1,1), datetime.date(2021,12,31)])