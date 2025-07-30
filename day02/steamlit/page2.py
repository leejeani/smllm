import streamlit as st

st.markdown("# Page 2 🎉")
st.sidebar.markdown("# Page 2 🎉")

def calculate_sum(n1, n2):
    return n1 + n2

st.title("Add numbers")

n1 = st.number_input("First Number")
n2 = st.number_input("Second Number")

if st.button("Calculate"):
    st.write("Summation is: " + str(calculate_sum(n1, n2)))

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
