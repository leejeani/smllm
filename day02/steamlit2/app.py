import streamlit as st

# Define the pages
main_page = st.Page("main.py", title="Main Page", icon="🎈")
page_1 = st.Page("page1.py", title="Page 1", icon="❄️")
page_2 = st.Page("page2.py", title="Page 2", icon="🎉")
page_3 = st.Page("page3.py", title="Page 3", icon="🎉")
page_4 = st.Page("page4.py", title="Page 4", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_1, page_2, page_3, page_4])

# Run the selected page
pg.run()