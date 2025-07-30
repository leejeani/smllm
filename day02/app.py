import streamlit as st

# Define the pages
main_page = st.Page("main.py", title="Main Page", icon="🎈")
page_1 = st.Page("s1.py", title="Page 1", icon="❄️")
page_2 = st.Page("s2.py", title="Page 2", icon="🎉")
page_3 = st.Page("s3.py", title="Page 3", icon="🎉")
page_4 = st.Page("s4.py", title="Page 4", icon="🎉")
page_5 = st.Page("s5.py", title="Page 5", icon="🎉")


# Set up navigation
pg = st.navigation([main_page, page_1, page_2, page_3,page_4,page_5])

# Run the selected page
pg.run()