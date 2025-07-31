import os
import time

import pandas as pd
import streamlit as st
from datetime import datetime

from PIL import Image

from llm.MyApi import openAiModel

# 선택한 파일을 저장하는 함수
def save_uploadedfile(directory, file):
    # 1. 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 2. 파일 저장 (이름 변경 없이 저장)
    st.info(file.name.split('.'))

    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    print(os.path.join(directory, file.name))
    print(file.name.split('.')[0])
    Image.open(os.path.join('images', file.name)).save(os.path.join('images', file.name.split('.')[0] + ".png"))

    # 3. 저장 완료 메시지 출력
    st.success(f'저장 완료: {directory}에 {file.name} 저장되었습니다.')


# 메인 함수
def main():
    st.markdown("# Page 4 🎉")
    st.sidebar.markdown("# Page 4 🎉")

    st.title('파일 업로드 예제')
    file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])

    if file:
        imgs = Image.open(file)
        save_uploadedfile('images', file)
        Image.open(os.path.join('images', file.name)).save(file.name.split('.')[0] + ".png")

        st.image(file)
        if st.button('send'):
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.08)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            client = openAiModel()
            response = client.images.create_variation(
                model="dall-e-2",
                image=open('images/'+file.name.split('.')[0]+".png", "rb"),
                n=3,
                size="512x512"
            )
            my_bar.empty()

            for n, data in enumerate(response.data):
                print(data.url)
                st.image(data.url)

            st.info('ok')

if __name__ == '__main__':
    main()