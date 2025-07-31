import os

import pandas as pd
import streamlit as st
from datetime import datetime

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")


# 선택한 파일을 저장하는 함수
def save_uploadedfile(directory, file):
    # 1. 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 2. 파일 저장 (이름 변경 없이 저장)
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())

    # 3. 저장 완료 메시지 출력
    st.success(f'저장 완료: {directory}에 {file.name} 저장되었습니다.')


# 메인 함수
def main():
    st.title('파일 업로드 예제')

    st.sidebar.title('사이드바')
    menu = ['이미지 파일 업로드', 'CSV 파일 업로드', 'PDF 파일 업로드']
    choice = st.sidebar.selectbox('메뉴를 선택하세요.', menu)

    if choice == menu[0]:  # 이미지 파일 업로드
        st.subheader(menu[0])
        file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])

        if file is not None:
            #new_filename = datetime.now().isoformat().replace(':', '_') + '.jpg'
            #file.name = new_filename  # 파일명 변경
            save_uploadedfile('images', file)
            st.image(file, use_container_width=True)

            st.download_button(
                label="💾 파일 다운로드",
                data=file,
                file_name=file.name,
                mime="image/jpeg"
            )
    elif choice == menu[1]:  # CSV 파일 업로드
        st.subheader(menu[1])
        file = st.file_uploader('CSV 파일 업로드', type=['csv'])

        if file is not None:
            save_uploadedfile('csv', file)
            df = pd.read_csv(file)
            st.dataframe(df)
            st.download_button(
                label="💾 파일 다운로드",
                data=file,
                file_name=file.name,
                mime="text/text"
            )

    elif choice == menu[2]:  # PDF 파일 업로드
        st.subheader(menu[2])
        file = st.file_uploader('PDF 파일 업로드', type=['pdf'])

        if file is not None:
            save_uploadedfile('pdf', file)
            #st.write(file)
#            with open(os.path.join('pdf', file.name), 'rb') as f:
#                audio_bytes = f.read()
            st.download_button(
                label="💾 파일 다운로드",
                data=file,
                file_name=file.name,
                mime="application/pdf"
            )

if __name__ == '__main__':
    main()