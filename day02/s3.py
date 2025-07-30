import streamlit as st

if st.button("클릭하세요"):
    st.write("버튼이 클릭되었습니다!")

agree = st.checkbox("동의합니다")
if agree:
  st.write("동의하셨습니다!")

selected_option = st.radio("옵션을 선택하세요", ("옵션 1", "옵션 2", "옵션 3"))
st.write(f"선택된 옵션: {selected_option}")

fruit = st.selectbox("과일을 선택하세요", ["사과", "바나나", "오렌지"])
st.write(f"선택한 과일: {fruit}")

planets = st.multiselect("행성을 선택하세요", ["목성", "화성", "해왕성"])
st.write(f"선택한 행성: {planets}")

number = st.slider("숫자를 선택하세요", 0, 50)
st.write(f"선택된 숫자: {number}")

rating = st.select_slider("평가를 선택하세요", ["나쁨", "보통", "좋음", "최고"])
st.write(f"선택한 평가: {rating}")