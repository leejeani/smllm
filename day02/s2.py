import streamlit as st

name = st.text_input(placeholder="이름을 입력하세요", label="이름")
st.write(f"입력된 이름: {name}")

age = st.number_input(placeholder="나이를 입력하세요", label="나이", min_value=0, max_value=100, step=1)
st.write(f"입력된 나이: {age}")

selected_date = st.date_input(label="가입일")
st.write(f"선택한 날짜: {selected_date}")

selected_time = st.time_input("시간 선택")
st.write(f"선택한 시간: {selected_time}")

message = st.text_area(placeholder="메시지를 입력하세요", label="메시지를 입력하세요")
st.write(f"입력된 메시지:\n{message}")

uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file is not None:
    st.write("업로드된 파일:", uploaded_file.name)

