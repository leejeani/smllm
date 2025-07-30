import streamlit as st
st.sidebar.title("사이드바 메뉴")
st.sidebar.markdown("# S1 page 🎈")
st.sidebar.markdown("여기에 설정을 추가할 수 있습니다.")
# 사이드바 요소 추가
option = st.sidebar.radio("옵션 선택", ["옵션 A", "옵션 B", "옵션 C"])
st.sidebar.button("사이드바 버튼")

st.title("Streamlit 웹 애플리케이션")
st.header("이것은 헤더입니다")
st.subheader("이것은 서브헤더입니다")
st.markdown("# 큰 제목 (Markdown)")
st.markdown("**굵은 글씨**와 *이탤릭체* 사용 가능")
st.caption("이것은 캡션(설명)입니다.")
st.code("""
        def hello():
            print("Hello, Streamlit!")
        """, language="python")
st.latex(r"E = mc^2")