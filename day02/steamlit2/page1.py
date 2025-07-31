import datetime
import time
import warnings

import streamlit as st
import pandas as pd

from llm.MyApi import openAiModel

def generate_responses(input_text, speech_file_path):  #llm이 답변 생성
    st.info(input_text)

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.08)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)


    client = openAiModel()
    response = client.audio.speech.create(
        model="tts-1",
        input=input_text,
        voice="alloy",
        response_format="mp3",
        speed=1.1,
    )
    response.stream_to_file(speech_file_path)
    my_bar.empty()

def main():
    st.markdown("# Page 1 ❄️")
    st.sidebar.markdown("# Page 1 ❄️")

    warnings.filterwarnings(action='ignore')

    speech_file_path = "tts_audio.mp3"
    text = st.text_area(label='질문 입력:', placeholder="질문을 입력하세요")  # 첫 페이지가 실행될 때 보여줄 질문
    if st.button('보내기'):
        if text:
            generate_responses(text)
            if speech_file_path:
                st.audio(speech_file_path, speech_file_path)
                with open(speech_file_path, 'rb') as f:
                    audio_bytes = f.read()
                    st.download_button(
                        label="💾 음성 파일 다운로드",
                        data=audio_bytes,
                        file_name="tts_audio.mp3",
                        mime="audio/mpeg"
                    )
        else:
            st.info('입력 하세요')

if __name__ == '__main__':
    main()